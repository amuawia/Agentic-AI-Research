# Study 002 Publication Figure Outputs

This directory contains public-safe, manuscript-oriented figures generated for Study 002. The figures support an operational benchmark framing: the reported `quality_score` values are workflow-generated operational quality proxies and should not be described as human evaluation ratings.

## Regeneration

Run the figure/table generation script from the repository root:

```bash
python3 research/study_002_foundation_model_comparison/analysis/scripts/generate_publication_figures_tables.py
```

The script reads the analysis-ready Study 002 workbook plus the operational-efficiency and task-stratified analysis outputs, then regenerates these PNG figures and the companion publication tables under `research/study_002_foundation_model_comparison/results/`.

## Figure catalog

| File | Manuscript use | Interpretation guardrail |
| --- | --- | --- |
| `figure_01_quality_heatmap_provider_workflow.png` | Provider × workflow quality-proxy heatmap | Treat cell values as operational proxy means, not validated human judgments. |
| `figure_02_quality_by_task_category.png` | Exploratory task-category comparison | The task bank is category-balanced; difficulty labels are secondary annotations. |
| `figure_03_cost_quality_tradeoff.png` | Cost versus quality-proxy tradeoff chart | Cost is an observed run-level metric and should not be generalized to stable production pricing. |
| `figure_04_operational_efficiency_ranking.png` | Configuration-level efficiency ranking | Efficiency combines workflow-generated quality proxy with observed cost/latency/token metrics. |

## Public-safety note

This directory is limited to reproducible scholarly outputs and does not contain private publication-planning material or access-sensitive operational details.
