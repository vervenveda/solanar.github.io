# Solanar TraceLab

Meteorological Scientific Annotation Studio.

## Core architecture
Solanar TraceLab uses two independent visual layers:

1. Guide layer — uploaded scientific image.
2. Annotation layer — learner interpretation.

The original source remains untouched while analysis stays separate above it.

## Scientific source images
Radar, satellite, synoptic, climate anomaly, model output, sounding, hurricane track, terrain/weather, SST, upper-air, or other meteorological maps.

## Annotation tools
Pen, arrows, labels, contour tracing, eraser, measurement, scientific colors, line width, solid/dashed/dotted line styles, guide opacity, zoom, before/after comparison.

## Meteorological symbols
Cold front, warm front, stationary front, occluded front, dryline, and trough.

## Measurement and scale
The learner defines a reference relationship such as:

`100 px = 100 km`

Measurements then use that calibration.

## Export
- Composite PNG
- Transparent annotation-overlay PNG
- Project JSON

Project JSON preserves the guide image, annotations, opacity, fit mode, and scale metadata.

## Pedagogic uses
Trace cold fronts, drylines, isobars, isotherms, cyclonic circulation, radar reflectivity structures, eyewalls, rainbands, outflow boundaries, hurricane tracks, SST anomalies, ENSO patterns, jet streaks, cloud shields, climate-model anomaly contours, sounding diagrams, and terrain/weather interactions.

## Privacy
Single-file vanilla HTML/CSS/JavaScript. Uploaded images stay local in the browser unless explicitly exported.

## Suggested repository path
`solanar.github.io/apps/Solanar_TraceLab_index.html`

Copyright © 2026 Jennifer Kay Pearl. All Rights Reserved.
