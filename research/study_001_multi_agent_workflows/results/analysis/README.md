# Analysis Dataset

This folder contains the cleaned analysis files used for evaluating the **main_001** experiment.

## Files

### main_001_checkpoint_90runs.csv

Raw exported experiment results after completing all workflow executions.

Contains:

* 9 pilot runs
* 90 main experiment runs
* Total: 99 workflow executions

---

### tasks.csv

Final task dataset used in the experiment.

Contains:

* 30 enterprise-oriented tasks
* Categories:

  * Knowledge
  * Reasoning
  * Coding
* Difficulty levels:

  * Easy
  * Medium
  * Hard

---

### main_001_analysis_dataset_v0.2.xlsx

Cleaned and merged analysis dataset prepared for statistical analysis.

Processing steps:

1. Removed pilot_001 runs.
2. Kept only main_001 runs.
3. Matched workflow executions to the task dataset.
4. Added task metadata:

   * real_task_id
   * category
   * difficulty
   * expected_output
5. Generated pivot tables and analysis sheets.

Final dataset size:

* 90 workflow executions
* 30 tasks
* 3 workflow architectures per task

---

### analysis_plan.md

Official analysis planning document.

This file defines:

- Dataset scope
- Workflow architectures
- Analysis methodology
- Evaluation metrics
- Statistical summaries
- Visualization requirements

Refer to this document for the complete analysis roadmap.

---

## Dataset Versions

### V0.1

Initial merged analysis dataset.

### V0.2

Corrected analysis dataset with manually verified **real_task_id** values and finalized task metadata.

**Status:** Frozen

---

## Workflow Types

The experiment evaluates three workflow architectures:

1. **basic_agent**
2. **planner_executor**
3. **planner_executor_reviewer**

---

## Analysis Scope

The analysis focuses on:

* Average confidence by workflow
* Standard deviation by workflow
* Confidence by task category
* Confidence by task difficulty
* Workflow improvement over the baseline workflow
* Statistical summaries and visualizations

---

## Final Analysis Outputs

The final analysis workbook contains the following sheets:

1. Main Dataset
2. Workflow Summary
3. Category Analysis
4. Difficulty Analysis
5. Improvement Analysis

---

## Notes

The original **task_id** field in the raw workflow results should not be used for analysis because all workflow executions used the same internal identifier during execution.

Use **real_task_id** from the merged task metadata instead.

---

## Related Project Assets

### Figures

Final visualizations are stored in:

```text
../figures/
```

Files:

* workflow_summary.png
* workflow_category.png
* workflow_difficulty.png
* workflow_improvement.png

### Documentation

Research documentation is stored in:

```text
../docs/
```

Planned documents:

* methodology.md
* results_summary.md
* discussion.md
* threats_to_validity.md

---

## Reproducibility

All workflow definitions, datasets, experiment results, and analysis artifacts are version-controlled within this repository to support reproducibility and future replication of the study.
