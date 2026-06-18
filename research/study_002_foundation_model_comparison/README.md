# Study 002: Foundation Model Comparison

## Overview

This study extends the findings of Study 001 by evaluating multi-agent AI workflow architectures across multiple foundation model providers using a controlled experimental design.

The study investigates how workflow architecture and model provider influence answer quality, confidence, execution cost, latency, token consumption, and overall task performance across enterprise AI workloads.

## Research Objective

To compare the performance of three workflow architectures across three leading foundation model providers using identical prompts, task definitions, workflow logic, evaluation metrics, and experimental procedures.

### Workflow Architectures

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

### Foundation Model Providers

* OpenAI (GPT-5.5)
* Google (Gemini 2.5 Pro)
* Anthropic (Claude Sonnet 4.6)

## Research Questions

### RQ1

How does workflow architecture affect task performance?

### RQ2

How do different foundation model providers perform under identical workflow architectures?

### RQ3

What are the trade-offs between quality, confidence, latency, token consumption, and cost?

### RQ4

Does the Planner–Executor–Reviewer architecture consistently improve answer quality compared to simpler architectures?

## Experimental Design

### Task Bank

The study uses a fixed task bank of 30 tasks covering:

* Knowledge Tasks
* Reasoning Tasks
* Coding Tasks

### Difficulty Levels

* Easy
* Medium
* Hard

### Experimental Matrix

| Factor                 | Levels |
| ---------------------- | ------ |
| Providers              | 3      |
| Workflow Architectures | 3      |
| Tasks                  | 30     |
| Total Runs             | 270    |

### Evaluation Metrics

* Quality Score
* Confidence Score
* Execution Duration
* Token Consumption
* Estimated Cost
* Workflow Complexity

## Official Dataset

### Collection Configuration

| Item             | Value                                                    |
| ---------------- | -------------------------------------------------------- |
| Workflow Version | V1.4.4                                                   |
| Prompt Version   | frozen_v1.1                                              |
| Task Bank        | task_bank_v1                                             |
| Providers        | OpenAI, Google, Anthropic                                |
| Workflow Types   | Basic Agent, Planner–Executor, Planner–Executor–Reviewer |
| Total Runs       | 270                                                      |

### Dataset Files

```text
datasets/openai/
Agentic_AI_Experiments_Main_OpenAI_V1.4.4_90Runs.xlsx

datasets/gemini/
Agentic_AI_Experiments_Main_Gemini_V1.4.4_90Runs.xlsx

datasets/claude/
Agentic_AI_Experiments_Main_Claude_V1.4.4_90Runs.xlsx

datasets/merged/
Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs.xlsx

datasets/merged/
Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx
```

## Data Collection Status

### Main Collection Status

| Provider  | Model             | Runs | Status   |
| --------- | ----------------- | ---- | -------- |
| OpenAI    | GPT-5.5           | 90   | Complete |
| Google    | Gemini 2.5 Pro    | 90   | Complete |
| Anthropic | Claude Sonnet 4.6 | 90   | Complete |

### Collection Summary

* Total Tasks: 30
* Total Workflow Configurations: 3
* Total Providers: 3
* Total Experimental Runs: 270

## Reliability Notes

### Retry Events

A small number of transient provider/API failures occurred during collection and were documented in:

```text
datasets/logs/retry_log.xlsx
```

Affected runs were rerun using the same:

* Provider
* Model
* Workflow Architecture
* Workflow Version
* Prompt Version

### Structured Output Compliance

One Claude Basic Agent run produced valid task content but failed JSON schema compliance after repeated execution attempts. The event was documented in the retry log and retained for reproducibility purposes.

## Repository Structure

```text
datasets/
workflows/
analysis/
figures/
results/
manuscript/
```

## Current Phase

### Statistical Analysis Phase

## Current Status

The Study 002 data collection phase is complete. The AnalysisReady dataset has been validated, descriptive statistics have been generated, reliability metrics have been documented, and formal assumption testing has been completed.

Current phase: Two-Way ANOVA and inferential statistical analysis.

### Completed

* Data collection completed
* Dataset validation completed
* Descriptive statistics completed
* Reliability metrics completed
* Statistical working workbook created
* Descriptive assumption assessment completed
* Formal assumption testing completed

### Assumption Testing Summary

Formal assumption testing was conducted for the primary outcome (`quality_score`) and secondary outcome (`confidence`). Shapiro-Wilk tests indicated departures from normality, and Levene’s tests indicated variance heterogeneity. Because the experimental design is balanced with equal cell sizes (n = 30 per provider × workflow group), Two-Way ANOVA was retained as the primary inferential analysis method, with results to be interpreted alongside effect sizes and post-hoc comparisons.

### Next Steps

* Conduct Two-Way ANOVA for provider, workflow, and provider × workflow effects
* Conduct post-hoc comparisons where applicable
* Calculate effect sizes
* Generate figures and publication-ready tables
* Prepare the Study 002 manuscript


## Workflow Governance

Official workflow version:

```text
V1.4.4
```

All official runs were collected using V1.4.4.

Earlier workflow versions are retained for archival and validation purposes only.

## Prompt Governance

Official prompt version:

```text
frozen_v1.1
```

The update from frozen_v1 to frozen_v1.1 introduced explicit confidence normalization requirements:

```text
Confidence must be a decimal value between 0.0 and 1.0.
```

No prompt modifications were made after official collection began.

## Planned Statistical Analysis

Analysis procedures are documented in:

```text
shared/methodology/study_002_statistical_analysis_plan.md
```

The analysis dataset contains:

* Provider
* Workflow Type
* Quality Score
* Confidence Score
* Duration
* Cost
* Token Usage
* Task Category
* Task Difficulty

## Planned Publication

Target venues include:

* IEEE conferences
* Peer-reviewed AI engineering journals
* Agentic AI systems research venues

## Related Study

### Study 001

Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n

DOI: 10.5281/zenodo.20606084
