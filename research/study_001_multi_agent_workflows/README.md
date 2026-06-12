# Agentic AI Research Project

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20606084.svg)](https://doi.org/10.5281/zenodo.20606084)

## Overview

This research project evaluates the effectiveness of different Agentic AI workflow architectures for enterprise-oriented tasks using n8n and Google Gemini.

The study investigates whether multi-agent workflows can improve performance, consistency, and confidence compared with a traditional single-agent approach.

---

## Research Objective

The primary objective of this study is to compare three agentic workflow architectures and measure their impact on task performance across different task categories and difficulty levels.

Research Question:

> How do multi-agent workflow architectures affect performance on enterprise-oriented AI tasks compared with a single-agent baseline?

---

## Workflow Architectures

### 1. Basic Agent

A single AI agent receives a task and produces a direct response.

### 2. Planner Executor

A Planner Agent first decomposes the task and generates an execution plan. An Executor Agent then performs the task based on the generated plan.

### 3. Planner Executor Reviewer

A Planner Agent generates a plan, an Executor Agent performs the task, and a Reviewer Agent evaluates the output and assigns a quality score.

---

## Experimental Setup

* Platform: n8n
* Model: Google Gemini
* Dataset Size: 30 Tasks
* Categories:

  * Knowledge
  * Reasoning
  * Coding
* Difficulty Levels:

  * Easy
  * Medium
  * Hard

Each task was executed on all three workflow architectures.

Total Runs:

* Pilot Runs: 9
* Main Experiment Runs: 90
* Total Executions: 99

---

## Key Findings

### Overall Confidence

| Workflow                  | Confidence |
| ------------------------- | ---------: |
| Basic Agent               |      0.950 |
| Planner Executor          |      0.980 |
| Planner Executor Reviewer |      0.987 |

### Largest Improvements

| Metric              | Planner Executor | Planner Executor Reviewer |
| ------------------- | ---------------: | ------------------------: |
| Overall Performance |           +3.16% |                    +3.89% |
| Reasoning Tasks     |          +10.00% |                   +11.25% |
| Hard Tasks          |           +9.38% |                   +10.16% |

Key observation:

> Multi-agent architectures produced the greatest improvements on reasoning-intensive and difficult tasks while providing only limited gains for coding tasks where the base model already performed strongly.

---

## Repository Structure

```text
Agentic-AI-Research/
│
├── dataset/
├── workflows/
├── results/
├── figures/
├── docs/
├── paper/
└── scripts/
```

---

## Documentation

### Dataset and Analysis

* results/
* results/analysis/

### Figures

* figures/workflow_summary.png
* figures/workflow_category.png
* figures/workflow_difficulty.png
* figures/workflow_improvement.png

### Research Documentation

* docs/methodology.md
* docs/results_summary.md
* docs/discussion.md
* docs/threats_to_validity.md

---

## Status

Current Phase:

**Data Collection: Completed**

**Data Analysis: Completed**

**Paper Writing: Completed**

**Zenodo Publication: Completed**

**Research Project Version: v1.0**


---

## Publication

This research has been published on Zenodo and assigned a permanent DOI.

DOI: https://doi.org/10.5281/zenodo.20606084

Zenodo Record: https://zenodo.org/records/20606084

Citation:

Ali, M. (2026).  
Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n.  
Zenodo.  
https://doi.org/10.5281/zenodo.20606084


## Author

Muawia Ali

Independent Researcher

ORCID: https://orcid.org/0009-0000-2549-9862

