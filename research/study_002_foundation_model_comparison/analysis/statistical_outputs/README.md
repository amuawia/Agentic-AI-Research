# Statistical Outputs

This directory contains finalized statistical output files for Study 002.

## Files

| File | Status | Description |
|-------------------------------|----------|----------------------------------------------------------|
| dataset_validation_report.xlsx| Complete | Dataset validation report for the AnalysisReady dataset. |
| descriptive_statistics.xlsx   | Complete | Descriptive statistics by provider, workflow, provider × workflow, task category, difficulty, and reliability metrics. |
| assumption_tests.xlsx         | Complete | Descriptive and formal assumption testing results, including Shapiro-Wilk normality tests and Levene’s homogeneity of variance tests. |
| anova_results.xlsx            | Complete | Inferential statistics results for provider, workflow, and provider × workflow effects. |
| effect_sizes.xlsx             | Complete | Partial eta squared effect size analysis and interpretation for all ANOVA effects. |
| measurement_validity_audit.xlsx | Complete | Audit of the relationship between `quality_score` and `confidence` across workflow/provider configurations. |
| robustness_sensitivity.xlsx | Complete | Robust descriptive sensitivity checks, including median/IQR summaries, bootstrap confidence intervals, IQR outlier sensitivity, reviewer vs non-reviewer comparison, and simple mean-difference contrasts. |

## Source Dataset

The finalized source dataset is located at:

`research/study_002_foundation_model_comparison/datasets/merged/Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx`

## Notes

The files in this directory represent finalized outputs used for reporting. Intermediate calculations and pivot tables are maintained separately in the working analysis workbook.


Study 002 assumption testing has been completed. Descriptive assessment and formal assumption tests were conducted for the primary outcome (`quality_score`) and secondary outcome (`confidence`). Shapiro-Wilk tests indicated departures from normality, and Levene’s tests indicated variance heterogeneity. Because the experimental design is balanced with equal cell sizes (n = 30 per provider × workflow group), Two-Way ANOVA was retained as the primary inferential analysis method, with results to be interpreted alongside effect sizes and post-hoc comparisons.

Current phase: Effect size analysis completed. Preparing publication-ready figures, tables, and manuscript results.

## Measurement Validity Audit

The measurement-validity audit documents how `quality_score` relates to `confidence` in the Study 002 workflow outputs.

This distinction is important because Basic Agent and Planner–Executor workflows do not include an independent reviewer stage. In the V1.4.4 workflow parsing logic, `quality_score` falls back to `confidence` when no parsed `quality_score` is emitted by the workflow output. In contrast, Planner–Executor–Reviewer workflows include a reviewer stage that emits a review-derived `quality_score`, allowing `quality_score` and `confidence` to diverge.

The audit supports cautious interpretation of `quality_score` as an operational quality proxy rather than an independent human judgment of answer quality.
