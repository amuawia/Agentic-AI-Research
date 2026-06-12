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

In Progress

**Objective**

Extend the original study by comparing workflow architectures across multiple foundation model providers:

* Google Gemini
* OpenAI GPT
* Anthropic Claude

The study maintains a consistent workflow design and task set to enable controlled cross-provider evaluation.

Target publication venues include peer-reviewed conferences and journals in artificial intelligence, software engineering, and enterprise systems.

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
