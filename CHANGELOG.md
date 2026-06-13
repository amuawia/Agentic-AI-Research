## V1.4.3 - 2026-06-13

### Changed
- Updated token and cost estimation methodology.
- Token estimation now covers all LLM calls in each workflow architecture.
- Planner, Executor, and Reviewer intermediate outputs are included in output token estimation.
- Cost estimation now uses total estimated input/output tokens across all workflow stages.

### Reason
This version improves methodological consistency for comparing Basic Agent, Planner–Executor, and Planner–Executor–Reviewer workflows.


# Changelog

All notable changes to this research repository are documented in this file.

The format is inspired by Keep a Changelog and adapted for academic research projects.

---

## [Unreleased]

### Planned

* Complete OpenAI data collection for Study 002.
* Implement Gemini workflows (V1.4.2).
* Implement Claude workflows (V1.4.2).
* Perform statistical analysis across providers and workflow architectures.
* Prepare manuscript submission for a peer-reviewed venue.

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
