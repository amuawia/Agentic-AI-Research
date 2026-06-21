# 3. Methodology

## 3.1 Study Objective and Positioning

The objective of Study 002 is to evaluate how foundation model provider and agentic workflow architecture are associated with operational outcomes in controlled AI workflow execution. The study is positioned as an exploratory operational benchmark rather than a definitive human-rated assessment of answer quality. Its purpose is to provide reproducible system-level evidence about provider × workflow configurations, including quality-proxy behavior, confidence, cost, duration, token consumption, and workflow complexity.

The study extends an earlier single-provider workflow comparison by introducing multiple foundation model providers while preserving the same task bank, prompt version, workflow definitions, and execution protocol. This design enables the analysis to distinguish provider-associated effects, workflow-associated effects, and provider × workflow interactions under a common experimental framework.

## 3.2 Experimental Design

The study used a balanced 3 × 3 factorial design. The two primary experimental factors were:

- **Foundation model provider:** OpenAI, Google, and Anthropic.
- **Workflow architecture:** Basic Agent, Planner–Executor, and Planner–Executor–Reviewer.

Each provider × workflow condition was evaluated on the same 30-task benchmark, producing 270 official runs. The design is balanced at the provider × workflow level, with 30 runs per cell. All runs used Workflow Version V1.4.4 and Prompt Version `frozen_v1.1`.

The controlled design was intended to reduce confounding from changing prompts, task definitions, workflow logic, or execution procedures. Consequently, observed differences are interpreted as associations with provider selection, workflow architecture, or their interaction within this experimental setting.

## 3.3 Benchmark Task Bank

The benchmark task bank consisted of 30 enterprise-oriented tasks. The accepted task-bank design was balanced across three primary task categories:

- 10 Knowledge tasks,
- 10 Reasoning tasks,
- 10 Coding tasks.

This category-balanced design was selected to cover different types of enterprise AI work while keeping the experiment operationally feasible. Difficulty labels were added later as a secondary annotation layer and were not used as the primary balancing criterion. Therefore, task-difficulty summaries are reported as exploratory stratified analyses rather than as evidence from a difficulty-balanced design.

Each task was executed under every provider × workflow condition. This ensured that provider and workflow comparisons were based on identical task requirements.

## 3.4 Agentic Workflow Architectures

Three workflow architectures were evaluated.

### 3.4.1 Basic Agent

The Basic Agent architecture represents direct single-stage execution. The task is submitted to the foundation model, and the model produces a response without an explicit planning or review stage. This architecture serves as the baseline workflow condition.

### 3.4.2 Planner–Executor

The Planner–Executor architecture separates planning from response generation. A planning stage first produces a structured approach to the task. The execution stage then uses this plan to generate the final response. This workflow is intended to support task decomposition and more organized answer generation.

### 3.4.3 Planner–Executor–Reviewer

The Planner–Executor–Reviewer architecture adds a review stage after planning and execution. The reviewer stage evaluates the generated output and can identify omissions, inconsistencies, or possible improvements. The final output is then produced after this review process. This architecture increases workflow complexity and typically requires additional model calls, duration, tokens, and cost.

## 3.5 Foundation Model Providers

The study evaluated three commercially available foundation model providers:

- OpenAI GPT-5.5,
- Google Gemini 2.5 Pro,
- Anthropic Claude Sonnet 4.6.

These providers were selected because they represent widely used contemporary foundation model ecosystems and are relevant to enterprise AI deployment. The study does not claim universal provider superiority. Instead, provider findings are interpreted as time-bounded observations for the specific model versions, prompts, workflows, and task bank evaluated.

## 3.6 Outcome Variables and Operational Metrics

The study measured both effectiveness-oriented and operational-efficiency outcomes.

The primary effectiveness-oriented variable was:

- **Operational quality proxy (`quality_score`)**.

The secondary effectiveness-oriented variable was:

- **Model-reported confidence (`confidence`)**.

Operational metrics included:

- estimated cost in USD,
- execution duration in seconds,
- total token consumption,
- model call count.

These operational metrics were included because workflow architecture can improve or degrade practical deployment value depending on cost, latency, and token requirements. For enterprise AI systems, a workflow with higher observed quality may still be less attractive if it requires substantially more time, tokens, or cost.

## 3.7 Operational Quality Proxy and Measurement Validity

The variable `quality_score` is interpreted as an operational workflow-generated quality proxy rather than as an independent human judgment of answer quality. This distinction is central to the methodology.

In the Basic Agent and Planner–Executor workflows, no independent reviewer stage was present. When no explicit `quality_score` was emitted by those workflows, the parser used model-reported confidence as the operational quality proxy. In the Planner–Executor–Reviewer workflow, the reviewer stage could emit a review-derived `quality_score`, allowing quality and confidence to diverge.

To make this measurement issue transparent, the study includes a measurement-validity audit. The audit reports the extent to which `quality_score` equals `confidence` across workflows, providers, and provider × workflow cells. The audit showed that quality and confidence were identical for all observations in Basic Agent and Planner–Executor workflows, while they were mostly distinct in the Planner–Executor–Reviewer workflow. Therefore, quality-related results are interpreted cautiously as operational proxy evidence, not as human-perceived answer quality.

## 3.8 Data Collection Procedure

Data collection followed a standardized execution protocol. All benchmark tasks were executed using frozen prompt templates, fixed workflow definitions, common task inputs, and structured output capture. Execution results recorded task metadata, provider and model identifiers, workflow type, prompt version, workflow version, output text, confidence, operational quality proxy, duration, token usage, estimated cost, model call count, status fields, and notes.

Provider-specific execution outputs were merged into a unified analysis-ready dataset. Dataset validation was performed to verify completeness, balance across provider × workflow conditions, consistency of key fields, and absence of missing values in primary analysis variables. The final analysis-ready dataset contained 270 successful runs.

## 3.9 Statistical and Analytical Procedures

The analysis pipeline combined inferential, descriptive, robustness, and operational-efficiency analyses.

First, descriptive statistics summarized outcomes by provider, workflow, and provider × workflow condition. Second, two-way ANOVA was used to estimate provider, workflow, and provider × workflow effects for the operational quality proxy and confidence. Effect sizes were reported using partial eta squared. Third, assumption testing was conducted, and results were interpreted alongside robustness and sensitivity checks because the primary outcome did not fully satisfy all parametric assumptions.

Additional analyses were added to strengthen journal readiness without collecting new data:

- **Measurement-validity audit:** quantified the relationship between `quality_score` and `confidence`.
- **Robustness and sensitivity analysis:** reported medians, interquartile ranges, bootstrap confidence intervals, trimmed means, outlier sensitivity, reviewer vs non-reviewer comparisons, and simple contrasts.
- **Task-stratified analysis:** summarized results by Knowledge, Reasoning, and Coding categories, and by secondary difficulty annotations.
- **Operational-efficiency analysis:** calculated quality proxy per dollar, per 1,000 tokens, and per second, plus cost, latency, and token multipliers.
- **Publication figures and tables:** generated reproducible visual and tabular outputs for manuscript preparation.

These analyses support a cautious interpretation of observed provider/workflow patterns while improving transparency about measurement scope, robustness, and practical deployment trade-offs.

## 3.10 Reproducibility Strategy

Reproducibility was treated as a core design requirement. The study preserved the task bank, prompt version, workflow version, analysis-ready dataset, statistical scripts, generated workbooks, publication tables, and publication figures in a version-controlled research repository.

The reproducibility package includes scripts for dataset validation, descriptive statistics, assumption testing, ANOVA, effect size estimation, measurement-validity auditing, robustness and sensitivity analysis, operational-efficiency analysis, task-stratified analysis, and publication figure/table generation. This enables readers and reviewers to trace reported results from the analysis-ready dataset to final outputs.

Exact behavioral replication of commercial foundation models cannot be guaranteed because model providers may update deployed systems over time. However, preserving the evaluated prompts, workflow definitions, task bank, model identifiers, datasets, and analysis scripts provides a reproducible record of the experimental configuration and analytical process used in this study.

## 3.11 Scope of Inference

The study's findings apply to the evaluated provider versions, workflow definitions, prompt version, task bank, and execution period. The results should not be interpreted as permanent rankings of foundation model providers or as evidence that one workflow architecture is universally superior across settings. Instead, the study provides controlled operational evidence that workflow architecture and provider selection can interact, and that operational efficiency must be considered alongside quality-proxy and confidence outcomes when designing agentic AI systems.
