# Changelog

All notable changes to this research repository are documented in this file.

The format is inspired by Keep a Changelog and adapted for academic research projects.

---

## [Unreleased]

### Added

* Completed Two-Way ANOVA for Study 002.
* Added Provider, Workflow, and Provider × Workflow significance testing for `quality_score`.
* Added Provider, Workflow, and Provider × Workflow significance testing for `confidence`.
* Added post-hoc comparison analysis.
* Added partial eta squared effect size estimates within ANOVA outputs.

### Updated

* Updated Study 002 status from assumption testing to effect size analysis and publication-ready result generation.

### Current Phase

* Effect size analysis and publication-ready result generation.




## Study 002 - Descriptive Statistics and Working Analysis Setup

### Added

- Dataset validation report for the Study 002 AnalysisReady dataset.
- Descriptive statistics workbook with overall, provider-level, workflow-level, task-level, and reliability summaries.
- Statistical outputs directory for finalized analysis results.
- Working analysis directory containing the statistical workbook for pivot tables and intermediate calculations.

### Updated

- Study 002 README with current analysis status and next steps.

### Git Tag

- study002-descriptive-statistics-complete

### Planned

* Conduct official Study 002 data collection.
* Complete 270 official runs across providers and workflow architectures.
* Perform descriptive and inferential statistical analysis.
* Calculate effect sizes and Provider × Workflow interaction effects.
* Prepare manuscript submission for a peer-reviewed venue.

---

## V1.4.4 - Official Pre-Collection Freeze - 2026-06-14

### Added

* Added markdown fence cleanup across all provider workflows.
* Added confidence normalization to constrain values to 0.0–1.0.
* Added quality score normalization to constrain values to 0.0–1.0.
* Added explicit prompt instruction requiring confidence as a decimal value between 0.0 and 1.0.
* Added provider model registry.
* Added Study 002 statistical analysis plan.
* Added V1.4.4 validation datasets for OpenAI, Gemini, and Claude.
* Added V1.4.4 workflow implementations for OpenAI, Gemini, and Claude.

### Changed

* Updated active workflows for OpenAI, Gemini, and Claude to V1.4.4.
* Updated Prompt Version from frozen_v1 to frozen_v1.1.
* Updated official run identifiers from `pilot_*` to `main_*` for official data collection.
* Standardized Provider and Model metadata across OpenAI, Gemini, and Claude workflows.
* Updated token and cost tracking methodology documentation.
* Updated Study 002 repository documentation and workflow governance records.

### Deprecated

* Deprecated V1.4.3 workflows after successful V1.4.4 validation.

### Validation

* Completed OpenAI pilot validation.
* Completed Gemini pilot validation.
* Completed Claude pilot validation.
* Completed V1.4.4 validation runs across all workflow architectures.
* Approved V1.4.4 as the official workflow version for Study 002 data collection.

### Notes

* No workflow architecture changes were introduced.
* No provider or model changes were introduced.
* V1.4.4 represents the official pre-collection freeze for Study 002.
* Official data collection will use Workflow Version V1.4.4 and Prompt Version frozen_v1.1.

---

## V1.4.3 - 2026-06-13

### Changed

* Updated token and cost estimation methodology.
* Token estimation now covers all LLM calls in each workflow architecture.
* Planner, Executor, and Reviewer intermediate outputs are included in output token estimation.
* Cost estimation now uses total estimated input/output tokens across all workflow stages.

### Reason

This version improves methodological consistency for comparing Basic Agent, Planner–Executor, and Planner–Executor–Reviewer workflows.

---

## [2026-06-12]

### Study 002 Initiated

#### Added

* Created Study 002: Foundation Model Comparison.
* Established experimental design comparing:

  * Google Gemini
  * OpenAI GPT
  * Anthropic Claude
* Standardized workflow architectures:

  * Basic Agent
  * Planner–Executor
  * Planner–Executor–Reviewer
* Created OpenAI workflow suite:

  * Basic Agent V1.4.2
  * Planner Executor V1.4.2
  * Planner Executor Reviewer V1.4.2
* Added experimental metrics:

  * Quality Score
  * Confidence Score
  * Duration
  * Token Consumption
  * Cost Estimation

#### Changed

* Reorganized repository into study-based structure.
* Separated published research from active studies.

---

## [2026-06-09]

### Study 001 Published

#### Published

Title:

Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n

DOI:

10.5281/zenodo.20606084

#### Added

* Published final manuscript.
* Published supporting datasets.
* Published workflow definitions.
* Created public research record on Zenodo.

---

## [2026-05]

### Study 001 Development

#### Added

* Initial workflow implementations.
* Experimental task dataset.
* Data collection and evaluation framework.
* Comparative workflow analysis methodology.

#### Evaluated

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

using Google Gemini models and n8n workflow orchestration.
