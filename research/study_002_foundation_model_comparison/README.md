# Study 002: Foundation Model Comparison

## Overview

This study extends the findings of Study 001 by evaluating multi-agent AI workflow architectures across multiple foundation model providers.

The goal is to assess how workflow design and model selection influence answer quality, confidence, execution cost, latency, and overall effectiveness across enterprise AI tasks.

## Research Objective

To compare the performance of three workflow architectures across multiple foundation model providers using a consistent experimental design.

### Workflow Architectures

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

### Foundation Model Providers

* OpenAI
* Google Gemini
* Anthropic Claude

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

### Tasks

The study uses a fixed task bank covering:

* Knowledge Tasks
* Reasoning Tasks
* Coding Tasks

### Difficulty Levels

* Easy
* Medium
* Hard

### Evaluation Metrics

* Quality Score
* Confidence Score
* Execution Duration
* Token Consumption
* Estimated Cost
* Workflow Complexity

## Repository Structure

```text
datasets/
workflows/
analysis/
figures/
results/
manuscript/
```

## Status

Pre-collection validation complete.

| Provider         | Model             | Workflow Version | Prompt Version | Pilot Status | V1.4.4 Validation |
| ---------------- | ----------------- | ---------------- | -------------- | ------------ | ----------------- |
| OpenAI           | GPT-5.5           | V1.4.4           | frozen_v1.1    | Complete     | Complete          |
| Google Gemini    | Gemini 2.5 Pro    | V1.4.4           | frozen_v1.1    | Complete     | Complete          |
| Anthropic Claude | Claude Sonnet 4.6 | V1.4.4           | frozen_v1.1    | Complete     | Complete          |

## Current Phase

Study 002 is ready for official data collection.

Official data collection will use:

* Workflow Version: V1.4.4
* Prompt Version: frozen_v1.1
* Dataset Version: task_bank_v1
* Providers: OpenAI, Google Gemini, Anthropic Claude
* Workflow Types: Basic Agent, Planner–Executor, Planner–Executor–Reviewer
* Expected Official Runs: 270

## Official Run Identifiers

Official data collection workflows use the `main_*` identifier prefix.

Examples:

* main_openai_v002
* main_gemini_v002
* main_claude_v002
* main_openai_v002_basic_agent
* main_openai_v002_planner_executor
* main_openai_v002_planner_executor_reviewer

Pilot identifiers remain archived for validation records only.

## Prompt Governance

Prompt Version: frozen_v1.1

The prompt set is frozen for official data collection.

The update from frozen_v1 to frozen_v1.1 added an explicit instruction requiring confidence values to be reported as decimals between 0.0 and 1.0.

No prompt changes are allowed after official data collection begins unless a new prompt version is created and documented.

## Workflow Governance

Official workflow version for Study 002 data collection: V1.4.4

V1.4.4 must be used consistently for OpenAI, Gemini, and Claude workflows.

Earlier workflow versions are retained for archival validation only and must not be mixed with official V1.4.4 analysis.


## Planned Publication

Peer-reviewed journal or conference submission.

## Related Study

Study 001:

Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n

DOI: 10.5281/zenodo.20606084


Prompt Set Version: 1.0
Status: Frozen

Frozen Date: 2026-06-12


Official workflow version for cross-provider pilots: V1.4.3

V1.4.3 must be used consistently for OpenAI, Gemini, and Claude workflows. Earlier V1.4.2 pilot outputs are retained for archival validation only and must not be mixed with official V1.4.3 analysis.


## Methodology Documentation

The study methodology is documented under:

- shared/methodology/evaluation_framework.md
- shared/methodology/scoring_rubric.md
- shared/methodology/token_cost_tracking.md
- shared/methodology/study_002_statistical_analysis_plan.md
