# Agentic AI Research

Research repository for evaluating and benchmarking multi-agent AI workflow architectures across enterprise tasks and foundation models.

## Overview

This repository contains research studies, datasets, workflows, analyses, and publications related to Agentic AI systems.

The project investigates how different workflow architectures perform across knowledge, reasoning, and coding tasks, with a focus on:

* Single-Agent (Basic Agent)
* Planner–Executor
* Planner–Executor–Reviewer

The research evaluates multiple foundation model providers, including:

* Google Gemini
* OpenAI GPT
* Anthropic Claude

Performance is assessed using quality, confidence, latency, token consumption, and cost metrics.

---

## Research Studies

### Study 001: Multi-Agent Workflow Architectures

**Title**

Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n

**Status**

Published

**DOI**

10.5281/zenodo.20606084

**Objective**

Evaluate the performance of three workflow architectures across enterprise AI tasks using Gemini-based agents.

---

### Study 002: Foundation Model Comparison

**Status**

Main data collection completed.

Current project phase:

* Statistical analysis in progress
* Dataset frozen for analysis
* Official collection completed: 270 runs

**Official Collection Configuration**

* Workflow Version: V1.4.4
* Prompt Version: frozen_v1.1
* Dataset Version: task_bank_v1
* Providers: OpenAI, Google Gemini, Anthropic Claude
* Workflows:

  * Basic Agent
  * Planner–Executor
  * Planner–Executor–Reviewer
* Total Official Runs: 270

**Dataset Summary**

| Provider         | Model             | Runs | Status   |
| ---------------- | ----------------- | ---- | -------- |
| OpenAI           | GPT-5.5           | 90   | Complete |
| Google Gemini    | Gemini 2.5 Pro    | 90   | Complete |
| Anthropic Claude | Claude Sonnet 4.6 | 90   | Complete |

**Dataset Artifacts**

* OpenAI Dataset: 90 runs
* Gemini Dataset: 90 runs
* Claude Dataset: 90 runs
* Merged Dataset: 270 runs
* AnalysisReady Dataset: Available

**Objective**

Extend the original Study 001 by comparing workflow architectures across multiple foundation model providers using a controlled experimental design.

Providers evaluated:

* Google Gemini
* OpenAI GPT
* Anthropic Claude

The study maintains a consistent workflow architecture, prompt set, task bank, evaluation framework, and workflow implementation across providers to enable controlled cross-provider comparison.

**Research Questions**

* RQ1: How does workflow architecture affect task performance?
* RQ2: How do different foundation model providers perform under identical workflow architectures?
* RQ3: What are the trade-offs between quality, confidence, latency, token consumption, and cost?
* RQ4: Does the Planner–Executor–Reviewer architecture consistently improve answer quality compared to simpler architectures?

**Experimental Design**

* Providers: 3
* Workflow Architectures: 3
* Tasks: 30
* Total Runs: 270

Task categories:

* Knowledge
* Reasoning
* Coding

Difficulty levels:

* Easy
* Medium
* Hard

**Current Activities**

* Descriptive statistics
* Provider comparison analysis
* Workflow comparison analysis
* Statistical hypothesis testing
* Figure and table generation
* Manuscript preparation

**Reliability Notes**

During collection, a small number of transient provider/API failures occurred and were documented in the project retry log.

One Claude Basic Agent run produced valid task content but failed JSON schema compliance after repeated execution attempts. The event was documented and retained for reproducibility purposes.

**Planned Publication**

Target venues include:

* IEEE conferences
* Peer-reviewed AI engineering journals
* Agentic AI systems research venues
* Enterprise AI and software engineering conferences

**Related Study**

Study 001:

*Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n*

DOI: 10.5281/zenodo.20606084


---

## Repository Structure

```text
research/
├── study_001_multi_agent_workflows/
└── study_002_foundation_model_comparison/

shared/
├── datasets/
├── prompts/
├── templates/
├── methodology/

docs/

scripts/

archive/
```

---

## Workflow Architectures

### Basic Agent

Single-agent execution where one model receives the task and produces the final answer.

### Planner–Executor

Two-stage workflow:

1. Planner generates a task plan.
2. Executor performs the task using the generated plan.

### Planner–Executor–Reviewer

Three-stage workflow:

1. Planner creates the execution plan.
2. Executor generates the solution.
3. Reviewer evaluates and improves the final result.

---

## Experimental Metrics

The research captures:

* Quality Score
* Confidence Score
* Execution Duration
* Token Consumption
* Estimated Cost
* Workflow Complexity

These metrics support comparative analysis of workflow architectures and foundation models.

---

## Reproducibility

All datasets, workflow definitions, prompts, and analysis artifacts required to reproduce published results are maintained in this repository whenever licensing and platform restrictions permit.

---

## Author

Muawia Ali

ORCID: 0009-0000-2549-9862

Website: https://muawia.com

---

## Citation

If you use this repository, datasets, workflows, or publications, please cite the relevant study and associated DOI where applicable.

See:

* CITATION.cff
* docs/citation.md

---

## License

See LICENSE for licensing information.
