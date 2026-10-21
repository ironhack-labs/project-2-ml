# Validation and execution notes

## Verified on 2026-10-15
- All three notebooks executed top-to-bottom in numerical order; all code cells completed without recorded execution errors.
- `pytest -q`: **1 passed** (`tests/test_data_pipeline.py`).
- Data loader: 5,005 usable rows across 26 source files and 9 test families.
- Grouped holdout: 3,692 training rows / 20 source files and 1,313 test rows / 6 source files; no source-file overlap.
- Training-only grouped cross-validation (mean ± fold SD MAE): Gradient Boosting 0.08013 ± 0.00124 V; Random Forest 0.08557 ± 0.01031 V; Extra Trees 0.09057 ± 0.01263 V; Ridge regression 0.14366 ± 0.00454 V; mean baseline 0.19817 ± 0.00123 V.
- Random Forest randomized search: best grouped-CV MAE 0.08206 V (40 trees, max depth 16, min samples leaf 4, max features 0.8).
- Held-out metrics: mean baseline MAE 0.19650 V, RMSE 0.22708 V, R² -0.00087; Ridge MAE 0.13707 V, RMSE 0.16292 V, R² 0.48481; Gradient Boosting MAE 0.07800 V, RMSE 0.10093 V, R² 0.80225; Random Forest MAE 0.06566 V, RMSE 0.09089 V, R² 0.83966; Extra Trees MAE 0.06497 V, RMSE 0.09116 V, R² 0.83870; tuned Random Forest MAE 0.06631 V, RMSE 0.09030 V, R² 0.84171.
- Notebook 3 successfully loaded the serialized tuned pipeline from `best_model.joblib`, generated demo predictions, and saved held-out comparison plots for MAE, RMSE, and R².
- Data plots include representative polarization curves, power-density curves, and median polarization profiles by test family. Model figures include grouped-CV metrics, tuning results, held-out model metrics, predicted-vs-observed, residuals, permutation importance, and segmented errors.

## Interpretation caution
This validation establishes reproducibility for the included archive and environment, not generalization to other laboratories or MEAs. File-grouped splitting is more conservative than random row splitting, but related test protocols may still occur in both partitions. The lowest score differs by metric: Extra Trees has the lowest held-out MAE, while tuned Random Forest has the lowest RMSE and highest R². Differences among tree ensembles are small and should not be framed as decisive.
