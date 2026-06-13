# Evaluation Framework

## Study

Study 002: Evaluating Multi-Agent Workflow Architectures Across Foundation Models: A Comparative Study of Gemini, GPT, and Claude Agents

## Objective

The objective of this study is to evaluate the effects of workflow architecture and foundation model provider on enterprise AI task performance while maintaining a consistent experimental design.

The study extends the findings of Study 001 by introducing multiple foundation model providers while preserving workflow structure, task design, and prompt governance.

---

# Research Questions

## RQ1

How does workflow architecture affect task performance?

## RQ2

How do foundation model providers perform under identical workflow architectures?

## RQ3

What trade-offs exist between quality, confidence, latency, token consumption, and cost?

## RQ4

Does the Planner–Executor–Reviewer architecture consistently improve performance compared to simpler architectures?

## RQ5

What proportion of performance variation is attributable to workflow architecture, foundation model provider, and their interaction?

---

# Experimental Design

## Independent Variables

### Provider

Levels:

* OpenAI
* Google Gemini
* Anthropic Claude

### Workflow Architecture

Levels:

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

---

# Task Dataset

Dataset Version:

task_bank_v1

Task Categories:

* Knowledge
* Reasoning
* Coding

Difficulty Levels:

* Easy
* Medium
* Hard

Total Tasks:

30

---

# Experimental Conditions

All providers must use:

* The same task dataset
* The same workflow logic
* The same prompt set version
* The same scoring methodology
* The same workflow version

Prompt Set Version:

frozen_v1

Workflow Version:

V1.4.3

---

# Dependent Variables

The following variables are collected for each run:

* Quality Score
* Confidence Score
* Duration (seconds)
* Input Tokens
* Output Tokens
* Total Tokens
* Estimated Cost (USD)
* Success Status

---

# Data Collection

Each task is executed independently under every provider and workflow combination.

Expected Design:

3 Providers × 3 Workflows × 30 Tasks

Expected Runs:

270

---

# Statistical Analysis

## Descriptive Statistics

For each metric:

* Mean
* Median
* Standard Deviation
* Minimum
* Maximum

## Comparative Analysis

Comparisons will be conducted across:

* Workflow architectures
* Foundation model providers

## Inferential Analysis

Primary analysis:

Two-Way ANOVA

Factors:

* Provider
* Workflow

Dependent Variables:

* Quality Score
* Confidence Score
* Duration
* Total Tokens
* Estimated Cost

Alternative non-parametric methods may be used if assumptions are violated.

## Effect Size

Effect sizes will be reported whenever appropriate.

Examples:

* Partial Eta Squared (η²)
* Cohen's d

## Interaction Analysis

Provider × Workflow interaction effects will be evaluated.

---

# Threats to Validity

## Internal Validity

Potential provider-specific prompt interpretation differences may affect outcomes.

Mitigation:

* Frozen prompt set
* Consistent workflow logic

## Construct Validity

Quality scores depend on the scoring rubric.

Mitigation:

* Standardized evaluation framework
* Explicit scoring rubric

## External Validity

Results are limited to:

* Selected providers
* Selected tasks
* Selected workflow architectures

## Reliability

Workflow automation and version control are used to improve reproducibility.

---

# Reproducibility

The following artifacts will be preserved:

* Workflow definitions
* Prompt sets
* Datasets
* Experimental outputs
* Statistical analysis scripts

All official experiments must be reproducible using the repository contents.
