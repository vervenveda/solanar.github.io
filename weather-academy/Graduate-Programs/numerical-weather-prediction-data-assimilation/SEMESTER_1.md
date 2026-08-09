# Graduate Semester I — Numerical Atmospheric Modeling

## Week 1 — Forecast Systems as Scientific Models
- **Monday — Theory & Model Formulation:** Frame NWP as a chain from observations → analysis → numerical integration → physics → products → verification; distinguish model state, analysis, forecast and post-processing.
- **Tuesday — Mathematics & Numerical Analysis:** Represent atmospheric variables as functions/state vectors and review dimensional consistency, Taylor expansion and error notation.
- **Wednesday — Computational Laboratory:** Build a reproducible experiment notebook and run baseline sensitivity calculations in the Solanar Numerical Prediction Lab.
- **Thursday — Operational NWP / DA Diagnosis:** Compare a current analysis and forecast product while identifying what is observed, assimilated, modeled and derived.
- **Friday — Research, Verification & Defense:** Write a graduate model-system map and identify at least five distinct uncertainty sources.
- **Higher Learning mathematics:** Calculus II, Linear Algebra
- **Required computational evidence:** Numerical Experiment Design Record, Computational Reproducibility Record

## Week 2 — Governing Equations & Model State
- **Monday — Theory & Model Formulation:** Revisit mass, momentum, thermodynamic and moisture equations as a coupled prediction system; examine hydrostatic versus nonhydrostatic modeling choices.
- **Tuesday — Mathematics & Numerical Analysis:** Express coupled prognostic variables as vectors/systems and analyze units, scales and dependencies.
- **Wednesday — Computational Laboratory:** Create a simplified coupled state-vector model and test parameter sensitivity.
- **Thursday — Operational NWP / DA Diagnosis:** Inspect operational model variable sets and diagnose which fields are prognostic versus diagnostic.
- **Friday — Research, Verification & Defense:** Defend which simplifications are acceptable for a toy educational model and which would invalidate its purpose.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra
- **Required computational evidence:** Model Configuration & Provenance Record, Numerical Experiment Design Record

## Week 3 — Grids, Coordinates & Discrete Atmospheric States
- **Monday — Theory & Model Formulation:** Study structured grids, staggering concepts, map projections, cubed-sphere ideas, vertical coordinates and resolution tradeoffs.
- **Tuesday — Mathematics & Numerical Analysis:** Translate continuous fields into indexed arrays/vectors; examine coordinate transforms and matrix representations.
- **Wednesday — Computational Laboratory:** Construct discrete 1-D/2-D fields and quantify how grid spacing changes representation of gradients/features.
- **Thursday — Operational NWP / DA Diagnosis:** Compare global and regional model grid/resolution choices and document consequences for resolved phenomena.
- **Friday — Research, Verification & Defense:** Research memo: resolution is not equivalent to forecast accuracy—explain why.
- **Higher Learning mathematics:** Linear Algebra, Calculus II
- **Required computational evidence:** Grid & Coordinate Analysis, Model Configuration & Provenance Record

## Week 4 — Finite Differences, Truncation Error & Consistency
- **Monday — Theory & Model Formulation:** Derive forward, backward and centered finite-difference approximations from Taylor expansion and classify truncation error.
- **Tuesday — Mathematics & Numerical Analysis:** Work derivative approximations and error-order calculations; connect consistency to convergence.
- **Wednesday — Computational Laboratory:** Numerically approximate derivatives of analytic functions and measure error as grid spacing changes.
- **Thursday — Operational NWP / DA Diagnosis:** Inspect how numerical derivative choices affect atmospheric gradient diagnostics.
- **Friday — Research, Verification & Defense:** Produce a convergence table and defend whether observed error reduction matches theoretical order.
- **Higher Learning mathematics:** Calculus II, Introduction to Proofs
- **Required computational evidence:** Numerical Stability & Error Analysis, Computational Reproducibility Record

## Week 5 — Time Integration, CFL Stability & Error Growth
- **Monday — Theory & Model Formulation:** Study explicit/implicit ideas, Euler and Runge–Kutta families, stability regions conceptually, CFL constraints and accumulated numerical error.
- **Tuesday — Mathematics & Numerical Analysis:** Analyze ODE time stepping and stability; calculate CFL numbers across atmospheric flow/grid/time-step scenarios.
- **Wednesday — Computational Laboratory:** Use the CFL lab to map stable/unstable combinations and compare numerical solutions to an analytic benchmark.
- **Thursday — Operational NWP / DA Diagnosis:** Relate operational model resolution/time step to computational and stability constraints without assuming one universal CFL rule.
- **Friday — Research, Verification & Defense:** Write an error-budget note separating initial-condition, model and numerical errors.
- **Higher Learning mathematics:** Differential Equations, Calculus II
- **Required computational evidence:** Numerical Stability & Error Analysis, Model Configuration & Provenance Record

## Week 6 — UNIT I QUALIFYING CHECKPOINT — Numerical Foundations
- **Monday — Theory & Model Formulation:** Synthesize forecast-system architecture, governing equations, grids, finite differences and stability.
- **Tuesday — Mathematics & Numerical Analysis:** Complete derivations and numerical-error/stability calculations under timed conditions.
- **Wednesday — Computational Laboratory:** Implement/modify a simple finite-difference numerical experiment and document reproducibility.
- **Thursday — Operational NWP / DA Diagnosis:** Diagnose an operational model configuration from published documentation.
- **Friday — Research, Verification & Defense:** Orally defend numerical choices; written, quantitative, computational and oral components each require ≥80%.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra, Introduction to Proofs
- **Required computational evidence:** Numerical Experiment Design Record, Numerical Stability & Error Analysis, Computational Reproducibility Record

## Week 7 — Advection: Upwind, Centered & Higher-Order Tradeoffs
- **Monday — Theory & Model Formulation:** Study numerical advection as a core atmospheric transport problem; compare diffusion, dispersion, phase error and monotonicity.
- **Tuesday — Mathematics & Numerical Analysis:** Derive/update finite-difference advection equations and analyze amplification/error behavior conceptually.
- **Wednesday — Computational Laboratory:** Run 1-D advection experiments with varying wind, grid spacing and time step; compare shape preservation and numerical diffusion.
- **Thursday — Operational NWP / DA Diagnosis:** Identify forecast features whose timing/amplitude can be sensitive to transport numerics.
- **Friday — Research, Verification & Defense:** Write a method comparison emphasizing tradeoffs rather than declaring a universally best scheme.
- **Higher Learning mathematics:** Differential Equations, Calculus II
- **Required computational evidence:** Numerical Stability & Error Analysis, Numerical Experiment Design Record

## Week 8 — Diffusion, Filters & Numerical Noise
- **Monday — Theory & Model Formulation:** Study physical versus numerical diffusion, computational modes, smoothing/filtering and conservation implications.
- **Tuesday — Mathematics & Numerical Analysis:** Analyze diffusion equations/eigenmodes conceptually and calculate scale-dependent damping.
- **Wednesday — Computational Laboratory:** Add controlled diffusion to a toy field and quantify noise suppression versus signal loss.
- **Thursday — Operational NWP / DA Diagnosis:** Evaluate when smoothing a model field can obscure genuine small-scale structure.
- **Friday — Research, Verification & Defense:** Research note: distinguish numerical stabilization from physical parameterization.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra
- **Required computational evidence:** Numerical Stability & Error Analysis, Computational Reproducibility Record

## Week 9 — Dynamical Cores & Conservation
- **Monday — Theory & Model Formulation:** Compare major dynamical-core design ideas including finite-volume, spectral/semi-Lagrangian and gridpoint approaches; emphasize conservation and computational tradeoffs.
- **Tuesday — Mathematics & Numerical Analysis:** Use integral/flux reasoning and matrix/vector operators to describe discrete conservation.
- **Wednesday — Computational Laboratory:** Perform a finite-volume-style conservation experiment on a toy control volume.
- **Thursday — Operational NWP / DA Diagnosis:** Study GFS/FV3 documentation context and identify model-core versus physics responsibilities.
- **Friday — Research, Verification & Defense:** Defend conservation diagnostics that should accompany numerical experiments.
- **Higher Learning mathematics:** Calculus II, Linear Algebra
- **Required computational evidence:** Model Configuration & Provenance Record, Numerical Stability & Error Analysis

## Week 10 — Vertical Coordinates & Atmospheric Columns
- **Monday — Theory & Model Formulation:** Examine pressure, sigma/terrain-following, hybrid and height-like vertical coordinates, layer interfaces and terrain interactions.
- **Tuesday — Mathematics & Numerical Analysis:** Transform/compare vertical-coordinate representations and discretized column operators.
- **Wednesday — Computational Laboratory:** Construct a model-column representation and test how vertical resolution changes depiction of inversions/jet layers.
- **Thursday — Operational NWP / DA Diagnosis:** Compare reported operational vertical-layer structures and implications for boundary layer/upper atmosphere.
- **Friday — Research, Verification & Defense:** Write a design memo selecting a vertical coordinate for a hypothetical regional model.
- **Higher Learning mathematics:** Calculus II, Linear Algebra
- **Required computational evidence:** Grid & Coordinate Analysis, Model Configuration & Provenance Record

## Week 11 — Physical Parameterizations I — Radiation, Surface & PBL
- **Monday — Theory & Model Formulation:** Analyze why unresolved/sub-grid physical processes require parameterization; focus on radiation, land-surface exchange and planetary boundary layer schemes.
- **Tuesday — Mathematics & Numerical Analysis:** Express flux/budget relationships and sensitivity to parameter changes.
- **Wednesday — Computational Laboratory:** Run parameter sensitivity thought experiments with controlled surface/flux changes.
- **Thursday — Operational NWP / DA Diagnosis:** Compare model guidance during a boundary-layer-sensitive forecast and identify likely parameterization influences.
- **Friday — Research, Verification & Defense:** Prepare a parameterization audit that distinguishes evidence from speculation.
- **Higher Learning mathematics:** Calculus II, Statistics
- **Required computational evidence:** Physical Parameterization Audit, Numerical Experiment Design Record

## Week 12 — UNIT II QUALIFYING CHECKPOINT — Dynamics & Physics
- **Monday — Theory & Model Formulation:** Synthesize advection/diffusion, dynamical cores, vertical coordinates and physical parameterizations.
- **Tuesday — Mathematics & Numerical Analysis:** Complete numerical-method and flux/conservation calculations.
- **Wednesday — Computational Laboratory:** Run a documented sensitivity experiment and assess numerical versus physical impacts.
- **Thursday — Operational NWP / DA Diagnosis:** Interpret an operational-model forecast difference using configuration evidence.
- **Friday — Research, Verification & Defense:** Defend model-design tradeoffs; checkpoint components each ≥80%.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra, Statistics
- **Required computational evidence:** Physical Parameterization Audit, Numerical Stability & Error Analysis, Computational Reproducibility Record

## Week 13 — Physical Parameterizations II — Microphysics & Convection
- **Monday — Theory & Model Formulation:** Study cloud microphysics and convection parameterization, scale awareness, explicit versus parameterized convection and gray-zone challenges.
- **Tuesday — Mathematics & Numerical Analysis:** Analyze sensitivity and categorical/continuous verification metrics for precipitation experiments.
- **Wednesday — Computational Laboratory:** Design a controlled microphysics/convection sensitivity experiment using supplied or archived outputs.
- **Thursday — Operational NWP / DA Diagnosis:** Compare precipitation guidance across model configurations/resolutions without attributing differences to a single scheme absent evidence.
- **Friday — Research, Verification & Defense:** Write a parameterization experiment proposal with falsifiable expectations.
- **Higher Learning mathematics:** Statistics, Differential Equations
- **Required computational evidence:** Physical Parameterization Audit, Numerical Experiment Design Record

## Week 14 — Initial & Boundary Conditions, Spin-Up & Balance
- **Monday — Theory & Model Formulation:** Study model initialization, lateral boundary conditions, digital/implicit balancing concepts, spin-up and adjustment.
- **Tuesday — Mathematics & Numerical Analysis:** Analyze perturbation propagation and boundary forcing in simple ODE/system examples.
- **Wednesday — Computational Laboratory:** Perturb a toy initial state and quantify forecast divergence over time.
- **Thursday — Operational NWP / DA Diagnosis:** Compare analyses/short forecasts to identify spin-up or boundary-related artifacts.
- **Friday — Research, Verification & Defense:** Write a forecast-system diagnostic distinguishing initialization error from model-physics error.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra
- **Required computational evidence:** Model Configuration & Provenance Record, Deterministic Model Verification

## Week 15 — Limited-Area & High-Resolution NWP
- **Monday — Theory & Model Formulation:** Examine nesting, regional models, convection-allowing resolution, boundary dependence, computational cost and predictability limits.
- **Tuesday — Mathematics & Numerical Analysis:** Compute resolution/cost scaling examples and spatial-error metrics.
- **Wednesday — Computational Laboratory:** Compare coarse and high-resolution outputs for terrain/convection features using matched verification periods.
- **Thursday — Operational NWP / DA Diagnosis:** Assess what high-resolution guidance adds—and what false precision it can create.
- **Friday — Research, Verification & Defense:** Create an operational-use rubric for high-resolution guidance.
- **Higher Learning mathematics:** Statistics, Calculus II
- **Required computational evidence:** Model Configuration & Provenance Record, Deterministic Model Verification

## Week 16 — Deterministic Verification & Object/Timing Error
- **Monday — Theory & Model Formulation:** Study bias, MAE, RMSE, anomaly correlation concepts, categorical scores and spatial/timing verification limitations.
- **Tuesday — Mathematics & Numerical Analysis:** Calculate deterministic scores and examine sensitivity to thresholds/rare events.
- **Wednesday — Computational Laboratory:** Verify a small multi-variable forecast set and separate amplitude, timing and displacement errors.
- **Thursday — Operational NWP / DA Diagnosis:** Compare two model systems fairly using matched cases/lead times.
- **Friday — Research, Verification & Defense:** Write a verification report that avoids cherry-picking metrics.
- **Higher Learning mathematics:** Statistics
- **Required computational evidence:** Deterministic Model Verification, Computational Reproducibility Record

## Week 17 — Reproducible NWP Experiment Design
- **Monday — Theory & Model Formulation:** Integrate scientific method, controlled experiments, code/data provenance, configuration management and versioned outputs.
- **Tuesday — Mathematics & Numerical Analysis:** Use statistical design, paired comparisons, uncertainty and reproducible calculation practices.
- **Wednesday — Computational Laboratory:** Create a complete experiment directory/manifest for a toy NWP study and independently reproduce it.
- **Thursday — Operational NWP / DA Diagnosis:** Audit an archived model comparison for uncontrolled differences.
- **Friday — Research, Verification & Defense:** Submit Semester I computational research proposal and preregister primary metrics.
- **Higher Learning mathematics:** Statistics, Introduction to Proofs
- **Required computational evidence:** Numerical Experiment Design Record, Computational Reproducibility Record

## Week 18 — SEMESTER I COMPREHENSIVE — Numerical Modeling
- **Monday — Theory & Model Formulation:** Cumulative examination in governing equations, discretization, stability, advection/diffusion, dynamical cores, parameterizations, initialization and verification.
- **Tuesday — Mathematics & Numerical Analysis:** Complete graduate numerical-analysis and differential-equation problems.
- **Wednesday — Computational Laboratory:** Implement and defend a reproducible toy forecast-model experiment.
- **Thursday — Operational NWP / DA Diagnosis:** Diagnose a model forecast using configuration and verification evidence.
- **Friday — Research, Verification & Defense:** Portfolio/oral defense. Each component independently ≥80%.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra, Statistics, Introduction to Proofs
- **Required computational evidence:** Model Configuration & Provenance Record, Numerical Stability & Error Analysis, Deterministic Model Verification, Computational Reproducibility Record
