#!/usr/bin/env python3
"""Procksee v0.1: bounded, allowlisted RSS relay for Solanar. Python stdlib only.

Run on an operator-controlled server: python3 tools/procksee/server.py
Do NOT deploy this as a public GitHub Pages executable; Pages serves static files.
"""
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen

FEEDS = {
    "nasa-earth": "https://earthobservatory.nasa.gov/feeds/earth-observatory.rss",
    "climate": "https://www.climate.gov/news-features/feed",
    "noaa": "https://www.noaa.gov/news-release/rss.xml",
    "un-climate": "https://news.un.org/feed/subscribe/en/news/topic/climate-change/feed/rss.xml",
    "science-environment": "https://www.sciencedaily.com/rss/earth_climate.xml",
}
ORIGINS = {s.strip() for s in os.getenv("PROCKSEE_ORIGINS", "https://vervenveda.com,https://vervenveda.github.io").split(",") if s.strip()}
CACHE_SECONDS = 600
MAX_BYTES = 512 * 1024
_cache = {}
_lock = threading.Lock()


class Handler(BaseHTTPRequestHandler):
    server_version = "Procksee/0.1"

    def respond(self, status, body, content_type="application/json; charset=utf-8", extra=None):
        origin = self.headers.get("Origin", "")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=60" if status == 200 else "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        if origin in ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path
        if path == "/health":
            return self.respond(200, b'{"service":"procksee","status":"ready"}')
        if not path.startswith("/v1/feeds/") or "?" in path or "#" in path:
            return self.respond(404, b'{"error":"Unknown endpoint"}')
        feed = path[len("/v1/feeds/"):]
        if feed not in FEEDS:
            return self.respond(404, b'{"error":"Feed not approved"}')
        now = time.monotonic()
        with _lock:
            entry = _cache.get(feed)
        if entry and now - entry[0] < CACHE_SECONDS:
            return self.respond(200, entry[1], "application/xml; charset=utf-8", {"X-Procksee-Cache": "HIT"})
        try:
            request = Request(FEEDS[feed], headers={"User-Agent": "Procksee/0.1 (Solanar weather learning; contact: vervenveda@proton.me)", "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml"})
            # No user-supplied destinations. Restrict redirects to HTTPS and approved hosts in production.
            with urlopen(request, timeout=7) as response:
                if response.url.split("/")[0] != "https:":
                    raise ValueError("Non-HTTPS redirect denied")
                data = response.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise ValueError("Response too large")
                if not data.lstrip().startswith(b"<"):
                    raise ValueError("Unexpected feed response")
            with _lock:
                _cache[feed] = (time.monotonic(), data)
            return self.respond(200, data, "application/xml; charset=utf-8", {"X-Procksee-Cache": "MISS"})
        except Exception:
            if entry:
                return self.respond(200, entry[1], "application/xml; charset=utf-8", {"X-Procksee-Cache": "STALE"})
            return self.respond(502, b'{"error":"Approved source unavailable"}')

    def do_OPTIONS(self):
        return self.respond(405, b'{"error":"Method not allowed"}')


if __name__ == "__main__":
    host = os.getenv("PROCKSEE_HOST", "127.0.0.1")
    port = int(os.getenv("PROCKSEE_PORT", "8765"))
    print(f"Procksee listening on {host}:{port} (operator-controlled local prototype)")
    ThreadingHTTPServer((host, port), Handler).serve_forever()
