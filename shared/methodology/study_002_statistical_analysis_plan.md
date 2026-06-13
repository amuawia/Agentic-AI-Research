# Statistical Analysis Plan (SAP)

## Study

Study 002

Evaluating Multi-Agent Workflow Architectures Across Foundation Models: A Comparative Study of Gemini, GPT, and Claude Agents

---

# Version Information

Statistical Analysis Plan Version: 1.0

Status: Frozen Prior to Official Data Collection

Effective Workflow Version: V1.4.3

Prompt Version: frozen_v1

Dataset Version: task_bank_v1

---

# Purpose

This Statistical Analysis Plan (SAP) defines the statistical procedures that will be used to analyze Study 002 data.

The purpose of this document is to:

* Reduce analytical bias
* Improve methodological transparency
* Improve reproducibility
* Define statistical methods before official data collection

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

## Factors

### Provider

Three levels:

* OpenAI GPT-5.5
* Google Gemini 2.5 Pro
* Anthropic Claude Sonnet 4.6

### Workflow

Three levels:

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

---

# Dataset Structure

Expected Design:

3 Providers × 3 Workflows × 30 Tasks

Expected Runs:

270

---

# Independent Variables

## Provider

Categorical

Levels:

* OpenAI
* Gemini
* Claude

## Workflow

Categorical

Levels:

* Basic
* Planner–Executor
* Planner–Executor–Reviewer

---

# Blocking Variable

## Task

Task ID will be retained during analysis.

Tasks represent repeated observations across providers and workflows.

Task effects will be considered during interpretation of results.

---

# Dependent Variables

## Primary Outcomes

### Quality Score

Range:

0.0–1.0

Primary performance metric.

### Confidence Score

Range:

0.0–1.0

Model self-reported confidence.

---

## Secondary Outcomes

### Duration

Measured in seconds.

### Input Tokens

Estimated token count.

### Output Tokens

Estimated token count.

### Total Tokens

Estimated token count.

### Estimated Cost

Estimated USD cost.

---

# Data Cleaning

The following checks will be performed before analysis.

## Missing Values

Identify missing values for:

* Quality Score
* Confidence Score
* Duration
* Token counts
* Cost

Missing values will be documented.

## Failed Executions

Rows with:

* API failures
* Invalid outputs
* Parsing failures

will be retained in the dataset and flagged.

Quality Score:

0.0

Confidence Score:

0.0

API Status:

Failure

---

# Descriptive Statistics

For each provider and workflow combination:

Calculate:

* Mean
* Median
* Standard Deviation
* Minimum
* Maximum

For:

* Quality Score
* Confidence Score
* Duration
* Total Tokens
* Estimated Cost

---

# Visualization

The following visualizations may be produced.

## Quality Score

* Box plots
* Mean comparison charts

## Confidence Score

* Box plots
* Mean comparison charts

## Cost

* Cost comparison charts

## Duration

* Duration comparison charts

## Token Usage

* Token comparison charts

---

# Assumption Checks

Before conducting ANOVA:

## Normality

Shapiro–Wilk Test

Applied to residuals where appropriate.

## Homogeneity of Variance

Levene's Test

Applied to dependent variables.

---

# Inferential Analysis

## Primary Analysis

### Two-Way ANOVA

Model:

Outcome ~ Provider + Workflow + Provider × Workflow

Dependent Variables:

* Quality Score
* Confidence Score
* Duration
* Total Tokens
* Estimated Cost

Independent Variables:

* Provider
* Workflow

Significance Level:

α = 0.05

---

# Post-Hoc Analysis

If significant main effects are detected:

## Tukey HSD

Provider Comparisons:

* OpenAI vs Gemini
* OpenAI vs Claude
* Gemini vs Claude

Workflow Comparisons:

* Basic vs Planner–Executor
* Basic vs Planner–Executor–Reviewer
* Planner–Executor vs Planner–Executor–Reviewer

---

# Interaction Analysis

Provider × Workflow interactions will be evaluated.

Purpose:

Determine whether workflow effectiveness differs across providers.

Examples:

* Does Planner–Executor–Reviewer improve performance equally for all providers?
* Does one provider benefit more from multi-agent workflows?

---

# Effect Size Analysis

Effect sizes will be reported for all significant effects.

Preferred Measures:

## Partial Eta Squared (η²)

For ANOVA effects.

Interpretation Guidelines:

* Small ≈ 0.01
* Medium ≈ 0.06
* Large ≈ 0.14

---

# Cost-Effectiveness Analysis

Exploratory analyses may include:

## Quality per Dollar

Quality Score / Estimated Cost

## Quality per Token

Quality Score / Total Tokens

## Quality per Second

Quality Score / Duration

These analyses are exploratory and supplementary.

---

# Alternative Analysis

If ANOVA assumptions are substantially violated:

Potential alternatives include:

* Kruskal–Wallis Tests
* Mann–Whitney U Tests
* Robust Statistical Methods

Any deviations from the primary analysis plan will be documented.

---

# Statistical Software

Analysis may be conducted using:

* Python
* Pandas
* SciPy
* Statsmodels
* JASP
* Jamovi
* R

Final software selection will be documented in the manuscript.

---

# Reporting Standards

Results should include:

* Sample sizes
* Means
* Standard deviations
* Test statistics
* p-values
* Effect sizes
* Confidence intervals where applicable

---

# Reproducibility

All analysis scripts should be preserved within the repository.

Recommended Location:

scripts/statistical_analysis/

Outputs should be reproducible from the published dataset.

---

# Deviations

Any deviation from this Statistical Analysis Plan must be documented in:

CHANGELOG.md

and described in the final manuscript.

---

# Approval Status

Current Status:

Approved for Study 002

Effective Date:

2026-06-13
