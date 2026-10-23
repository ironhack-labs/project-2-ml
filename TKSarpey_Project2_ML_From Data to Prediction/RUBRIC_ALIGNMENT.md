# Official Project 2 rubric alignment

The course brief and full rubric are included as `COURSE_TEMPLATE_README.md` and `RUBRIC.md` for reference. This project uses the permitted bring-your-own-dataset route.

| Rubric criterion | Project evidence | Remaining caveat |
|---|---|---|
| 1. Problem framing | Notebook 01 defines target, user, decision, MAE/RMSE rationale; Notebook 03 discusses limits and recommendation | Error tolerance must ultimately be agreed with domain stakeholders |
| 2. Data preparation | Loader filters schema, converts numeric fields, removes non-finite target/features, documents derived-column leakage; imputers in pipeline | Missingness is protocol-dependent and should be investigated with subject-matter context |
| 3. Exploratory analysis | Target distribution, polarization relationship, humidity relationship, file sizes, summary statistics | Heterogeneous protocols limit causal interpretation |
| 4. Modelling and validation | Deterministic grouped holdout; grouped CV; Dummy, Ridge, Random Forest, Extra Trees; randomized tuning on training data; pipelines | Classification threshold criterion is not applicable to this regression task |
| 5. Evaluation and interpretation | Held-out MAE/RMSE/R², predicted-vs-observed, residuals, segmented errors, permutation importance, saved/reloaded pipeline | Full execution is required before citing final metrics |
| 6. Visualisation | EDA, CV comparison with spread, predicted-vs-observed and residual charts, importance chart | Review generated figures after a full run for legibility in slides |
| 7. Code quality | Reusable loader in `src/project_utils.py`, fixed seed, clear file structure | Verify all notebooks run top-to-bottom in the target environment |
| 8. Git/GitHub | `.gitignore` provided; commit history cannot be generated in a ZIP | User must create meaningful commits/branches in their Git repository |
| 9. Documentation | Project-specific README, comments/docstrings, attribution, requirements, rubric alignment | Fill presentation with actual run metrics after execution |
| 10. Presentation/demo | `PRESENTATION_OUTLINE.md`, Notebook 03 reload-and-predict demo | Live timing/rehearsal must be performed by presenter |

## Verification status
All three notebooks were executed top-to-bottom in numerical order on 2026-10-15 with no cell errors. The data-pipeline test passed (`1 passed`). Actual grouped-CV and held-out metrics are documented in `README.md` and `VALIDATION_NOTES.md`. The saved pipeline was reloaded and generated demo predictions. Git/GitHub commit-history and the live presentation are inherently user-side deliverables and cannot be manufactured by this ZIP.
