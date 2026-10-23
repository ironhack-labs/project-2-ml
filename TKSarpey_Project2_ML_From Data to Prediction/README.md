# Project 2 — PEM Fuel-Cell Voltage Prediction

This presents an organized outline of the executed PEMFC machine-learning project to follow the section-by-section structure of the three original Project 2 notebook templates. The project question, data source, grouped validation design, regression models, and interpretation remain specific to the PEM fuel-cell dataset.

## Start here

Run the notebooks in order from the project root:

1. `notebooks/01_eda_and_baseline.ipynb` — frame the task, load and inspect the data, audit quality and leakage, explore target/features, split by complete source file, and establish a grouped-CV baseline.
2. `notebooks/02_pipelines_and_models.ipynb` — recreate the same split, build preprocessing pipelines, compare model families using the same GroupKFold folds, tune Random Forest on training data only, and save `best_model.joblib`.
3. `notebooks/03_evaluation_and_interpretation.ipynb` — evaluate the saved model and baseline on held-out source files, inspect residuals and segmented errors, calculate permutation importance, and demonstrate loading the saved pipeline.

The notebook headings and section order follow the supplied templates:
- `01_eda_and_baseline.ipynb`
- `02_pipelines_and_models.ipynb`
- `03_evaluation_and_interpretation.ipynb`

## Research question and design

**Question:** Can cell voltage be predicted from current density and recorded operating context when complete source files are held out?

- **Target:** `cell_voltage` (V), a regression target.
- **Predictors:** `current_density`, `pressure`, `relative_humidity`, `test_family`, and `operating_set`.
- **Group identifier:** `source_file`, used for splitting and segmented diagnostics, not as a predictor.
- **Leakage prevention:** `power_density` is excluded because it is derived from current density and cell voltage.
- **Primary metric:** MAE in volts; RMSE and R² are complementary metrics.
- **Split:** deterministic 22% group holdout with `random_state=42`.
- **Model selection:** GroupKFold cross-validation on training source files; preprocessing and tuning happen inside the training workflow.

## Dataset and attribution

Source: Hamidi, S.; Haghighi, S.; Askari, K. *Dataset of Standard Tests of Nafion 112 Membrane and Membrane Electrode Assembly (MEA) Activation Tests of Proton Exchange Membrane (PEM) Fuel Cell*. ChemRxiv (2020). DOI: [10.26434/chemrxiv.11902023](https://doi.org/10.26434/chemrxiv.11902023).

The included source archive contains a license file identifying CC BY 4.0. Retain attribution and consult `data/raw/LICENSE` for reuse conditions. The loader scans the raw archive and selects polarization CSVs with the required columns; EIS tables are not mixed into the modelling dataset.

## Output files

Notebook execution creates or updates:
- `baseline_grouped_cv.csv`
- `results_model_comparison.csv`
- `tuning_results.csv`
- `best_model.joblib`
- `final_test_metrics.csv`
- `final_test_predictions.csv`
- `segmented_error_analysis.csv`
- `permutation_importance.csv`
- figures for the target distribution, feature relationships, grouped-CV comparison, tuning, prediction diagnostics, segmented error, and permutation importance.

Figures from the earlier project run that are retained for the presentation include representative polarization and power-density curves.

## Important interpretation notes

- Grouped holdout is more realistic than a random row split because complete source files are held out, but it is not independent-laboratory validation.
- Test families and operating conditions may be confounded.
- Permutation importance describes predictive reliance, not causality.
- The held-out test is for final reporting, not iterative model selection.
- The model is a research-screening aid, not a substitute for electrochemical testing or a validated engineering control system.

## Environment

Install dependencies from the project root:

```bash
python -m pip install -r requirements.txt
```

Then launch Jupyter and execute the three notebooks in numerical order.
