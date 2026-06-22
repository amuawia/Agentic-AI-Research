# 9. Reproducibility Package

Reproducibility represents an important challenge in contemporary foundation model research due to the rapid evolution of commercial AI systems, provider-side model updates, and differences in experimental implementation. To improve transparency and facilitate future verification efforts, Study 002 was designed with reproducibility as a core methodological objective.

The study preserved workflow definitions, prompt templates, benchmark tasks, datasets, analytical outputs, and publication assets within a version-controlled research repository. This approach provides traceability from raw experimental executions to the final results reported in the manuscript and enables independent examination of the experimental process.

## 9.1 Repository Structure

All study materials were maintained within the Study 002 research directory:

```text
research/study_002_foundation_model_comparison/
```

The repository includes dedicated folders for datasets, workflow definitions, statistical analysis, publication assets, and manuscript preparation.

Key components include:

* Provider-specific datasets
* Merged datasets
* Benchmark task bank
* Execution logs
* Workflow definitions
* Analysis scripts
* Statistical outputs
* Publication tables
* Publication figures
* Manuscript materials

This structure was intended to separate data collection, analysis, reporting, and documentation activities while preserving traceability across all stages of the research process.

## 9.2 Version-Controlled Experimental Assets

To minimize procedural drift during experimentation, all major experimental assets were frozen prior to official data collection.

The study used:

* Workflow Version V1.4.4
* Prompt Version frozen_v1.1
* task_bank_v1

These assets remained unchanged throughout the official experimental phase.

Version control was maintained through Git-based repository management. Experimental milestones, data collection phases, statistical analyses, and manuscript development activities were documented through commits and tagged releases. This process provides a documented history of project evolution and supports independent review of the research workflow.

## 9.3 Datasets and Data Preservation

Provider-specific results were preserved as separate datasets for OpenAI, Google Gemini, and Anthropic Claude. These datasets were subsequently merged into a unified experimental dataset and an analysis-ready dataset used for statistical evaluation.

The primary frozen dataset used throughout the analytical phase was:

Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx

This dataset contains 270 validated observations and served as the source for all descriptive statistics, assumption tests, inferential analyses, effect size calculations, tables, and figures reported in the study.

Maintaining a frozen analysis dataset reduces the possibility of inadvertent modifications during later analytical stages and supports consistent replication of reported findings.

## 9.4 Analytical Reproducibility

All major analytical procedures were preserved through dedicated analysis scripts and documented output files.

The analytical workflow included:

* Dataset validation
* Descriptive statistics
* Assumption testing
* Formal assumption testing
* Analysis of variance
* Effect size estimation
* Measurement-validity auditing
* Robustness and sensitivity analysis
* Task-stratified analysis
* Operational-efficiency analysis

Supporting scripts were retained within:

```text
analysis/scripts/
```

while generated outputs were preserved within:

```text
analysis/statistical_outputs/
```

This approach improves transparency by allowing analytical outputs to be traced back to specific processing steps and statistical procedures.

## 9.5 Publication Assets

Publication-oriented assets were generated directly from the validated analysis dataset and preserved separately from intermediate analytical outputs.

The repository includes:

* Publication tables
* Publication figures
* Statistical summaries

Final manuscript-facing publication figures were maintained within:

```text
results/figures_publication/
```

while publication tables were preserved as both spreadsheet and Markdown summaries:

```text
results/publication_tables_v2.xlsx
results/publication_tables_v2.md
```

Separating publication assets from intermediate analytical work reduces the likelihood of inconsistencies between reported findings and underlying statistical results.

The four current publication figures report: (1) mean operational quality proxy by provider × workflow, (2) quality proxy by task category, (3) cost–quality trade-off by provider × workflow, and (4) operational-efficiency ranking. These files are reporting artifacts generated from the validated dataset and should be interpreted using the measurement-validity limitations described in the manuscript.

## 9.6 Execution Logging and Traceability

Operational transparency was supported through structured execution logging.

Execution logs documented workflow executions, retry events, operational anomalies, and collection activities. These records provided an auditable history of data collection and enabled verification of execution outcomes during dataset validation.

Documented operational events included retry activity associated with Google Gemini executions and a JSON compliance failure observed during Anthropic Claude experimentation. These events were preserved within study logs and incorporated into validation procedures.

The retention of execution records improves transparency regarding the practical realities of large-scale evaluations involving commercial foundation model APIs.

## 9.7 Reproducibility Limitations

Despite extensive documentation and preservation efforts, exact replication of foundation model behavior cannot be guaranteed.

Commercial providers may introduce model updates, inference optimizations, pricing changes, or infrastructure modifications that alter system behavior over time. Consequently, future replications conducted using nominally identical workflows and prompts may not reproduce identical outputs.

This limitation reflects a broader challenge in empirical foundation model research rather than a limitation unique to the present study.

Accordingly, the reproducibility package should be interpreted as preserving the experimental procedures, datasets, analytical methods, and reporting pipeline associated with the evaluated systems at the time of experimentation.

## 9.8 Summary

The Study 002 reproducibility package was designed to support transparency, traceability, and independent verification. Through version-controlled workflows, frozen prompts, preserved benchmark tasks, validated datasets, documented analytical procedures, execution logs, and publication assets, the study provides a comprehensive record of the experimental and analytical process.

These materials strengthen confidence in the reported findings and support future replication, extension, and comparative research involving agentic workflow architectures and foundation model providers.
