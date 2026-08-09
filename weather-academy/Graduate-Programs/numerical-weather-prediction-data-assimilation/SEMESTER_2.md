# Graduate Semester II — Data Assimilation, Ensembles & Hybrid Prediction

## Week 19 — Observing Systems, Representativeness & Quality Control
- **Monday — Theory & Model Formulation:** Map surface, radiosonde, aircraft, buoy, radar, satellite and other observations into the DA problem; distinguish instrument, representativeness and preprocessing errors.
- **Tuesday — Mathematics & Numerical Analysis:** Model observations as noisy measurements of a state and introduce observation operators.
- **Wednesday — Computational Laboratory:** Build an observation inventory and perform QC/outlier experiments on synthetic observations.
- **Thursday — Operational NWP / DA Diagnosis:** Examine GDAS observation categories and operational data formats/context.
- **Friday — Research, Verification & Defense:** Defend an observation inclusion/exclusion decision using metadata and uncertainty.
- **Higher Learning mathematics:** Statistics, Linear Algebra
- **Required computational evidence:** DA Observation Inventory & QC, Computational Reproducibility Record

## Week 20 — Estimation, Bayesian Reasoning & Least Squares
- **Monday — Theory & Model Formulation:** Frame DA as statistical estimation combining prior/background and observations with uncertainty.
- **Tuesday — Mathematics & Numerical Analysis:** Derive scalar weighted-estimate/least-squares results and connect Bayesian/BLUE interpretations.
- **Wednesday — Computational Laboratory:** Use synthetic priors/observations to test sensitivity to assumed error variance.
- **Thursday — Operational NWP / DA Diagnosis:** Interpret analysis increments as evidence-weighted corrections rather than direct observations.
- **Friday — Research, Verification & Defense:** Write an assumptions ledger for a simple assimilation problem.
- **Higher Learning mathematics:** Statistics, Linear Algebra
- **Required computational evidence:** Innovation / Residual Diagnostics, Kalman / Ensemble DA Experiment

## Week 21 — Optimal Interpolation & BLUE
- **Monday — Theory & Model Formulation:** Develop Best Linear Unbiased Estimation / optimal interpolation concepts, gain weighting and multivariate covariance influence.
- **Tuesday — Mathematics & Numerical Analysis:** Solve scalar and small matrix OI/BLUE problems.
- **Wednesday — Computational Laboratory:** Implement a small matrix analysis update using prescribed background/observation errors.
- **Thursday — Operational NWP / DA Diagnosis:** Map the conceptual method to historical/modern DA evolution without implying current systems are simple OI.
- **Friday — Research, Verification & Defense:** Verify posterior error reduction and identify failure when covariance assumptions are wrong.
- **Higher Learning mathematics:** Linear Algebra, Statistics
- **Required computational evidence:** Variational DA Analysis, Error Covariance Audit

## Week 22 — 3D-Var & Cost-Function Minimization
- **Monday — Theory & Model Formulation:** Formulate 3D-Var as minimization of background and observation misfit terms at an analysis time.
- **Tuesday — Mathematics & Numerical Analysis:** Work quadratic cost functions, gradients and matrix-weighted norms.
- **Wednesday — Computational Laboratory:** Minimize a low-dimensional 3D-Var toy cost function and compare with BLUE solution under equivalent assumptions.
- **Thursday — Operational NWP / DA Diagnosis:** Interpret analysis increments and innovation diagnostics in an operational context.
- **Friday — Research, Verification & Defense:** Defend control variables/error assumptions and document convergence.
- **Higher Learning mathematics:** Linear Algebra, Statistics, Calculus II
- **Required computational evidence:** Variational DA Analysis, Innovation / Residual Diagnostics

## Week 23 — 4D-Var, Model Constraint & Time-Window Assimilation
- **Monday — Theory & Model Formulation:** Extend variational assimilation through time using a forecast model and time-distributed observations.
- **Tuesday — Mathematics & Numerical Analysis:** Analyze constrained optimization and sensitivity across a time window; introduce tangent-linear/adjoint reasoning.
- **Wednesday — Computational Laboratory:** Perform a simplified multi-time-step assimilation experiment and trace how early-state adjustments affect later observation fit.
- **Thursday — Operational NWP / DA Diagnosis:** Compare conceptual strengths/limitations of 3D-Var and 4D-Var.
- **Friday — Research, Verification & Defense:** Write a design memo selecting an assimilation window for a hypothetical system.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra, Calculus II
- **Required computational evidence:** Variational DA Analysis, Tangent-Linear / Adjoint Reasoning Log

## Week 24 — UNIT III QUALIFYING CHECKPOINT — Variational Assimilation
- **Monday — Theory & Model Formulation:** Synthesize observations/QC, estimation, OI/BLUE, 3D-Var and 4D-Var.
- **Tuesday — Mathematics & Numerical Analysis:** Complete matrix/statistical/optimization calculations.
- **Wednesday — Computational Laboratory:** Execute and document a toy variational analysis experiment.
- **Thursday — Operational NWP / DA Diagnosis:** Interpret innovations/increments and identify suspect assumptions.
- **Friday — Research, Verification & Defense:** Orally defend an assimilation design; components each ≥80%.
- **Higher Learning mathematics:** Linear Algebra, Statistics, Differential Equations
- **Required computational evidence:** Variational DA Analysis, Innovation / Residual Diagnostics, Computational Reproducibility Record

## Week 25 — Kalman Filtering & Sequential State Estimation
- **Monday — Theory & Model Formulation:** Develop forecast-analysis cycling, Kalman gain, covariance propagation and sequential updates.
- **Tuesday — Mathematics & Numerical Analysis:** Derive scalar Kalman equations and solve low-dimensional matrix cases.
- **Wednesday — Computational Laboratory:** Use the Solanar Kalman lab to vary prior/observation uncertainties and track posterior estimates.
- **Thursday — Operational NWP / DA Diagnosis:** Relate cycling analysis/forecast concepts to operational DA without oversimplifying nonlinear high-dimensional systems.
- **Friday — Research, Verification & Defense:** Produce a sensitivity report on covariance assumptions.
- **Higher Learning mathematics:** Linear Algebra, Statistics, Differential Equations
- **Required computational evidence:** Kalman / Ensemble DA Experiment, Error Covariance Audit

## Week 26 — Ensemble Kalman Filters
- **Monday — Theory & Model Formulation:** Study ensemble-estimated covariance, finite-ensemble sampling error, localization and inflation concepts.
- **Tuesday — Mathematics & Numerical Analysis:** Compute ensemble mean/covariance and simplified gain/update calculations.
- **Wednesday — Computational Laboratory:** Run an ensemble update experiment and test localization/inflation thought experiments.
- **Thursday — Operational NWP / DA Diagnosis:** Compare ensemble and variational information pathways.
- **Friday — Research, Verification & Defense:** Write a failure-mode analysis for small ensembles and mis-specified observations.
- **Higher Learning mathematics:** Linear Algebra, Statistics
- **Required computational evidence:** Kalman / Ensemble DA Experiment, Error Covariance Audit

## Week 27 — Hybrid Ensemble–Variational Assimilation
- **Monday — Theory & Model Formulation:** Examine why operational systems combine ensemble flow-dependent covariance with variational frameworks.
- **Tuesday — Mathematics & Numerical Analysis:** Blend static/ensemble covariance concepts and analyze weighting sensitivity.
- **Wednesday — Computational Laboratory:** Construct a simplified hybrid covariance experiment.
- **Thursday — Operational NWP / DA Diagnosis:** Study current NCEP hybrid ensemble-variational context and identify conceptual links to GFS initialization.
- **Friday — Research, Verification & Defense:** Defend when flow-dependent covariance should materially change an analysis.
- **Higher Learning mathematics:** Linear Algebra, Statistics
- **Required computational evidence:** Error Covariance Audit, Variational DA Analysis

## Week 28 — Background & Observation Error Covariance
- **Monday — Theory & Model Formulation:** Study spatial/cross-variable covariance, correlation length scales, representativeness, localization and observation-error correlation.
- **Tuesday — Mathematics & Numerical Analysis:** Estimate covariance/correlation from synthetic samples and inspect positive-definiteness/sampling issues conceptually.
- **Wednesday — Computational Laboratory:** Build competing covariance models and compare resulting analysis increments.
- **Thursday — Operational NWP / DA Diagnosis:** Use innovation statistics to diagnose possible error-model problems.
- **Friday — Research, Verification & Defense:** Research note: why 'smaller error' is not automatically a more truthful covariance model.
- **Higher Learning mathematics:** Statistics, Linear Algebra
- **Required computational evidence:** Error Covariance Audit, Innovation / Residual Diagnostics

## Week 29 — Bias Correction, Observation Operators & Radiance Assimilation
- **Monday — Theory & Model Formulation:** Examine systematic observation/model bias, nonlinear observation operators and direct radiance assimilation concepts.
- **Tuesday — Mathematics & Numerical Analysis:** Model bias terms and nonlinear mappings in simplified estimation exercises.
- **Wednesday — Computational Laboratory:** Compare assimilation with/without a controlled bias and diagnose posterior impacts.
- **Thursday — Operational NWP / DA Diagnosis:** Study ECMWF training themes on radiance observations and bias correction.
- **Friday — Research, Verification & Defense:** Write a bias-correction governance memo addressing overfitting and changing observing systems.
- **Higher Learning mathematics:** Statistics, Linear Algebra
- **Required computational evidence:** DA Observation Inventory & QC, Innovation / Residual Diagnostics

## Week 30 — UNIT IV QUALIFYING CHECKPOINT — Ensemble & Hybrid DA
- **Monday — Theory & Model Formulation:** Synthesize Kalman/EnKF, hybrid methods, covariance, bias correction and observation operators.
- **Tuesday — Mathematics & Numerical Analysis:** Complete matrix/covariance/probability calculations.
- **Wednesday — Computational Laboratory:** Run a controlled ensemble/hybrid toy assimilation experiment.
- **Thursday — Operational NWP / DA Diagnosis:** Diagnose innovations/spread and identify an error-model failure.
- **Friday — Research, Verification & Defense:** Defend the analysis and uncertainty treatment; all components ≥80%.
- **Higher Learning mathematics:** Linear Algebra, Statistics, Differential Equations
- **Required computational evidence:** Kalman / Ensemble DA Experiment, Error Covariance Audit, Innovation / Residual Diagnostics

## Week 31 — Ensemble Prediction, Perturbations & Stochastic Physics
- **Monday — Theory & Model Formulation:** Study initial-condition ensembles, model-error representation, stochastic physics, spread-skill relationships and scenario interpretation.
- **Tuesday — Mathematics & Numerical Analysis:** Calculate ensemble summary statistics, probabilities and spread/error measures.
- **Wednesday — Computational Laboratory:** Use the ensemble lab to calculate threshold probabilities and scenario sensitivity.
- **Thursday — Operational NWP / DA Diagnosis:** Examine current GEFS context and distinguish ensemble members from independent truths.
- **Friday — Research, Verification & Defense:** Create a probabilistic guidance brief that communicates low-probability/high-impact scenarios.
- **Higher Learning mathematics:** Statistics, Linear Algebra
- **Required computational evidence:** Ensemble Prediction & Probability Brief, Deterministic Model Verification

## Week 32 — Calibration, Post-Processing & Probabilistic Verification
- **Monday — Theory & Model Formulation:** Study reliability, sharpness, discrimination, Brier-score concepts, quantile/probability calibration and statistical post-processing.
- **Tuesday — Mathematics & Numerical Analysis:** Calculate probabilistic verification examples and simple regression/calibration adjustments.
- **Wednesday — Computational Laboratory:** Calibrate a synthetic ensemble forecast and test performance on held-out cases.
- **Thursday — Operational NWP / DA Diagnosis:** Compare raw versus calibrated guidance while preserving traceability.
- **Friday — Research, Verification & Defense:** Write a verification protocol that prevents training/test leakage.
- **Higher Learning mathematics:** Statistics
- **Required computational evidence:** Ensemble Prediction & Probability Brief, Deterministic Model Verification, Computational Reproducibility Record

## Week 33 — Reanalysis & Coupled Earth-System Data Assimilation
- **Monday — Theory & Model Formulation:** Study reanalysis principles and coupled atmosphere–ocean–land–ice initialization; examine consistency versus changing observing systems.
- **Tuesday — Mathematics & Numerical Analysis:** Analyze cycling, covariance and time-series concepts relevant to long reanalyses/coupled systems.
- **Wednesday — Computational Laboratory:** Compare analysis/reanalysis time series and identify observing-system discontinuity risks.
- **Thursday — Operational NWP / DA Diagnosis:** Connect operational coupled modeling and DA research to Earth-system prediction.
- **Friday — Research, Verification & Defense:** Prepare a coupled-DA research proposal identifying state variables and cross-component interactions.
- **Higher Learning mathematics:** Statistics, Differential Equations, Linear Algebra
- **Required computational evidence:** Numerical Experiment Design Record, Error Covariance Audit

## Week 34 — AI/ML in the NWP & DA Workflow
- **Monday — Theory & Model Formulation:** Evaluate ML for emulation, bias/model-error correction, observation processing, hybrid forecasting and DA support; distinguish learned prediction from physically based integration.
- **Tuesday — Mathematics & Numerical Analysis:** Study train/validation/test design, generalization, loss functions, uncertainty and baseline comparison using existing Statistics foundations.
- **Wednesday — Computational Laboratory:** Compare a simple learned correction to a baseline on held-out synthetic/model-error data.
- **Thursday — Operational NWP / DA Diagnosis:** Analyze where an ML component could enter a forecast/DA workflow and what operational safeguards are required.
- **Friday — Research, Verification & Defense:** Produce an ML/hybrid evaluation plan addressing physical consistency, distribution shift, uncertainty and reproducibility.
- **Higher Learning mathematics:** Statistics, Linear Algebra, Introduction to Proofs
- **Required computational evidence:** ML / Hybrid Prediction Evaluation, Computational Reproducibility Record

## Week 35 — Graduate Forecast-System Capstone Integration
- **Monday — Theory & Model Formulation:** Integrate a toy dynamical model, numerical solver, synthetic observations, assimilation method, ensemble/scenario generation and verification.
- **Tuesday — Mathematics & Numerical Analysis:** Choose/justify numerical and statistical methods and quantify uncertainty/error.
- **Wednesday — Computational Laboratory:** Complete the reproducible system build and controlled experiments.
- **Thursday — Operational NWP / DA Diagnosis:** Compare toy-system behavior to operational NWP/DA concepts without claiming production equivalence.
- **Friday — Research, Verification & Defense:** Submit manuscript-style capstone, source/data manifest, verification suite and oral-defense deck.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra, Statistics, Introduction to Proofs
- **Required computational evidence:** Graduate Forecast-System Capstone Record, Computational Reproducibility Record, Deterministic Model Verification

## Week 36 — GRADUATE QUALIFYING FINAL — Numerical Prediction & Data Assimilation
- **Monday — Theory & Model Formulation:** Complete cumulative examination spanning numerical modeling, physical parameterization, DA, ensembles, verification and hybrid AI/ML.
- **Tuesday — Mathematics & Numerical Analysis:** Complete independent numerical-analysis, matrix/DA and probabilistic calculations.
- **Wednesday — Computational Laboratory:** Perform a timed computational practical modifying/testing the toy forecast-assimilation system.
- **Thursday — Operational NWP / DA Diagnosis:** Diagnose an unseen model/analysis failure using innovations, ensembles, verification and configuration evidence.
- **Friday — Research, Verification & Defense:** Defend the capstone system and research conclusions. Written science, quantitative exam, coding/computational practical, DA diagnostic case and research/oral defense each independently ≥80%.
- **Higher Learning mathematics:** Differential Equations, Linear Algebra, Statistics, Introduction to Proofs
- **Required computational evidence:** Graduate Forecast-System Capstone Record, Computational Reproducibility Record, Innovation / Residual Diagnostics
