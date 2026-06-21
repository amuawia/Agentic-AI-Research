# Study 002 Reproducibility Runbook

This public-safe runbook documents how to regenerate the main Study 002 analysis outputs, statistical workbooks, and publication assets from the frozen analysis-ready dataset. It is intended to support journal-review transparency without including private submission-selection, publication-fee, or editorial-response strategy.

## Scope and interpretation

Study 002 is treated as a controlled exploratory operational benchmark. The `quality_score` field should be interpreted as an operational workflow-generated quality proxy rather than an independent human rating. In Basic Agent and Planner–Executor workflows, the parser may use `confidence` as the fallback quality proxy when no independent reviewer score is emitted; the Planner–Executor–Reviewer workflow can emit a review-derived quality score.

Task-category analyses use the benchmark's planned category balance across Knowledge, Reasoning, and Coding tasks. Difficulty labels are secondary annotation layers and should not be described as a primary balancing criterion.

## Prerequisites

Run commands from the repository root:

```bash
cd /path/to/Agentic-AI-research
```

The scripts use dependency-light Python where possible. The current reproducibility path requires Python 3 and `openpyxl`; publication figure generation also requires `Pillow`.

## Frozen input dataset

Primary input workbook:

```text
research/study_002_foundation_model_comparison/datasets/merged/Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx
```

Expected dataset shape: 270 official runs from 3 providers × 3 workflows × 30 benchmark tasks.

## Regenerating analysis outputs

Run these scripts from the repository root:

```bash
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_assumption_tests.py
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_anova.py
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_effect_sizes.py
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_measurement_validity_audit.py
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_robustness_sensitivity.py
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_operational_efficiency.py
python3 research/study_002_foundation_model_comparison/analysis/scripts/run_task_stratified_analysis.py
```

Expected output workbooks:

```text
research/study_002_foundation_model_comparison/analysis/statistical_outputs/assumption_tests.xlsx
research/study_002_foundation_model_comparison/analysis/statistical_outputs/anova_results.xlsx
research/study_002_foundation_model_comparison/analysis/statistical_outputs/effect_sizes.xlsx
research/study_002_foundation_model_comparison/analysis/statistical_outputs/measurement_validity_audit.xlsx
research/study_002_foundation_model_comparison/analysis/statistical_outputs/robustness_sensitivity.xlsx
research/study_002_foundation_model_comparison/analysis/statistical_outputs/operational_efficiency.xlsx
research/study_002_foundation_model_comparison/analysis/statistical_outputs/task_stratified_analysis.xlsx
```

## Regenerating publication figures and tables

After the analysis workbooks exist, regenerate manuscript-facing assets:

```bash
python3 research/study_002_foundation_model_comparison/analysis/scripts/generate_publication_figures_tables.py
```

Expected figure outputs:

```text
research/study_002_foundation_model_comparison/results/figures_publication/figure_01_quality_heatmap_provider_workflow.png
research/study_002_foundation_model_comparison/results/figures_publication/figure_02_quality_by_task_category.png
research/study_002_foundation_model_comparison/results/figures_publication/figure_03_cost_quality_tradeoff.png
research/study_002_foundation_model_comparison/results/figures_publication/figure_04_operational_efficiency_ranking.png
```

Expected table outputs:

```text
research/study_002_foundation_model_comparison/results/publication_tables_v2.xlsx
research/study_002_foundation_model_comparison/results/publication_tables_v2.md
```

## Verification checklist

After regeneration, verify that:

1. All expected workbooks and figure files exist.
2. Workbook sheet names can be opened with `openpyxl`.
3. Figure files have non-zero dimensions and readable PNG metadata.
4. Public outputs contain only reproducibility material and exclude non-public submission-planning notes.
5. Staged files do not include `.hermes/` or `research/study_001_multi_agent_workflows/`.

A minimal verification command is:

```bash
python3 - <<'PY'
from pathlib import Path
from openpyxl import load_workbook
from PIL import Image
root = Path('research/study_002_foundation_model_comparison')
for path in [
    root/'analysis/statistical_outputs/robustness_sensitivity.xlsx',
    root/'analysis/statistical_outputs/operational_efficiency.xlsx',
    root/'analysis/statistical_outputs/task_stratified_analysis.xlsx',
    root/'results/publication_tables_v2.xlsx',
]:
    wb = load_workbook(path, read_only=True, data_only=True)
    print(path, wb.sheetnames)
for path in sorted((root/'results/figures_publication').glob('*.png')):
    with Image.open(path) as img:
        print(path, img.size)
PY
```

## Reporting guardrails

When using these outputs in the manuscript, describe observed patterns cautiously as associations within a controlled exploratory benchmark. Efficiency rankings are descriptive summaries of the evaluated configurations, not causal rankings or provider-wide claims.
