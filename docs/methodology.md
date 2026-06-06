# Methodology

## Research Design

This study evaluates the effectiveness of different Agentic AI workflow architectures for enterprise-oriented tasks. The objective is to determine whether multi-agent workflows improve performance, confidence, and consistency compared with a traditional single-agent approach.

A comparative experimental design was used to evaluate three workflow architectures under identical conditions.

---

## Experimental Environment

The workflows were implemented using n8n and executed using Google Gemini as the underlying large language model.

All workflow executions used:

* The same task dataset
* The same workflow infrastructure
* The same execution environment
* The same evaluation process

This ensured that differences in performance could be attributed primarily to workflow architecture rather than environmental factors.

---

## Workflow Architectures

### Basic Agent

The Basic Agent workflow consists of a single AI agent that receives a task prompt and generates a direct response.

Workflow:

```text
Task → Agent → Response
```

---

### Planner Executor

The Planner Executor workflow separates planning from execution.

Workflow:

```text
Task → Planner → Execution Plan → Executor → Response
```

The Planner Agent generates a structured plan which is then executed by the Executor Agent.

---

### Planner Executor Reviewer

The Planner Executor Reviewer workflow introduces an additional review stage.

Workflow:

```text
Task → Planner → Executor → Reviewer → Final Response
```

The Reviewer Agent evaluates the generated response and assigns a quality score.

---

## Dataset Construction

A custom dataset of 30 enterprise-oriented tasks was created for the experiment.

Tasks were designed to represent realistic business and technical scenarios.

The dataset was divided into three categories:

### Knowledge

Tasks requiring factual understanding, comparison, explanation, or summarization.

### Reasoning

Tasks requiring analysis, planning, decision-making, or multi-step problem solving.

### Coding

Tasks requiring software development, scripting, debugging, or technical implementation.

---

## Difficulty Classification

Each task was assigned a difficulty level:

* Easy
* Medium
* Hard

Difficulty levels were determined based on the expected cognitive complexity and number of reasoning steps required to complete the task.

---

## Experimental Procedure

Each task was executed on all three workflow architectures.

The experiment consisted of:

### Pilot Phase

* 9 pilot executions
* Used for workflow validation and debugging

### Main Experiment

* 30 tasks
* 3 workflow architectures per task
* Total executions: 90

The pilot runs were excluded from the final analysis.

---

## Data Collection

Workflow outputs were automatically logged using Google Sheets integration.

Collected data included:

* workflow_type
* task prompt
* response
* execution summary
* confidence score
* quality score (Reviewer workflow only)

The exported results were stored as CSV files and later merged with task metadata.

---

## Data Preparation

The final analysis dataset was created through the following process:

1. Remove pilot executions.
2. Retain only main experiment runs.
3. Match task prompts to the task dataset.
4. Assign verified task identifiers.
5. Add category metadata.
6. Add difficulty metadata.
7. Generate the final analysis dataset.

The resulting dataset contained:

* 90 workflow executions
* 30 unique tasks
* 3 workflow architectures

---

## Evaluation Metrics

The primary evaluation metric was confidence score.

Confidence scores were analyzed across:

* Workflow architecture
* Task category
* Difficulty level

For the Planner Executor Reviewer workflow, reviewer-generated quality scores were also recorded.

Additional evaluation metrics included:

* Average confidence
* Minimum confidence
* Maximum confidence
* Standard deviation
* Percentage improvement over baseline

---

## Statistical Analysis

The analysis was conducted using Microsoft Excel.

Pivot tables and descriptive statistics were used to evaluate:

1. Workflow performance.
2. Category-specific performance.
3. Difficulty-specific performance.
4. Improvement relative to the Basic Agent baseline.

Visualizations were generated to summarize experimental findings.

---

## Reproducibility

All datasets, workflow definitions, analysis files, figures, and documentation are maintained within the project repository.

Version-controlled artifacts allow future researchers to reproduce the experiment and verify the reported results.
