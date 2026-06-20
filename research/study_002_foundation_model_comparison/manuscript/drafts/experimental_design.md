# 4. Experimental Design

## 4.1 Factorial Design

The study employed a controlled factorial experimental design to evaluate the effects of foundation model provider and workflow architecture on agentic AI system performance.

Two primary independent variables were examined:

1. Foundation model provider
2. Workflow architecture

Three levels were evaluated for each variable. Foundation model providers consisted of OpenAI GPT-5.5, Google Gemini 2.5 Pro, and Anthropic Claude Sonnet 4.6. Workflow architectures consisted of Basic Agent, Planner–Executor, and Planner–Executor–Reviewer.

The resulting design produced nine provider-workflow combinations. Each combination was evaluated using an identical benchmark task set, resulting in a total of 270 official experimental executions.

The factorial structure enabled assessment of:

* Main effects associated with provider selection
* Main effects associated with workflow architecture
* Interaction effects between provider and workflow

This design was selected to support direct statistical comparison of the relative contributions of model selection and workflow design.

## 4.2 Foundation Model Providers

The study evaluated three commercially available foundation model providers representing leading contemporary large language model ecosystems.

The evaluated models were:

* OpenAI GPT-5.5
* Google Gemini 2.5 Pro
* Anthropic Claude Sonnet 4.6

Provider selection was motivated by their widespread adoption, advanced reasoning capabilities, and relevance to enterprise AI applications.

Each provider was evaluated under identical workflow conditions using the same benchmark tasks, workflow logic, and prompt templates. This approach minimized procedural differences and improved comparability across experimental conditions.

Official data collection was organized into three provider-specific collections:

* main_openai_v002
* main_gemini_v002
* main_claude_v002

Each provider contributed 90 official observations to the final dataset.

## 4.3 Workflow Architectures

Three workflow architectures were evaluated.

### Basic Agent

The Basic Agent workflow represents a single-stage execution process in which a task is submitted directly to the foundation model and a response is generated without explicit planning or review mechanisms.

This workflow served as the baseline condition for comparison.

### Planner–Executor

The Planner–Executor workflow separates problem-solving into planning and execution phases. The planning stage generates a structured strategy for completing the task, while the execution stage performs the requested work according to the generated plan.

This architecture was designed to encourage task decomposition and structured reasoning.

### Planner–Executor–Reviewer

The Planner–Executor–Reviewer workflow extends the previous architecture through the addition of a review stage. Following execution, a reviewer component evaluates the generated output and provides feedback intended to improve completeness and consistency.

The final response is produced after incorporating the review process.

All workflows were implemented using Workflow Version V1.4.4 and remained unchanged throughout official experimentation.

## 4.4 Benchmark Task Bank

Performance was evaluated using a benchmark consisting of 30 enterprise-oriented tasks.

The benchmark was organized into three task categories:

* Knowledge
* Reasoning
* Coding

These categories were selected to represent common forms of enterprise AI work while providing diversity in cognitive and technical requirements.

Tasks were sourced from task_bank_v1 and remained unchanged throughout the study. The use of a frozen benchmark ensured that all providers and workflows were evaluated against identical task requirements.

The benchmark also incorporated multiple difficulty levels:

* Easy
* Medium
* Hard

Difficulty assignments were inherited from the benchmark design and were not modified during experimentation.

## 4.5 Experimental Conditions

Each benchmark task was executed under every provider-workflow combination.

This procedure ensured complete coverage of the experimental design and produced a balanced allocation across the primary independent variables.

The final experimental design consisted of:

* 3 providers
* 3 workflow architectures
* 30 benchmark tasks

Resulting in:

* 270 official executions

Provider allocation was balanced, with 90 executions per provider.

Workflow allocation was also balanced, with 90 executions per workflow architecture.

Task category allocation was balanced across the final dataset, resulting in equal representation of Knowledge, Reasoning, and Coding tasks.

Difficulty distribution reflected the composition of the benchmark task bank and therefore was not perfectly balanced. The final dataset contained:

* 63 Easy observations
* 99 Medium observations
* 108 Hard observations

This imbalance was intentional because the benchmark itself was preserved without modification.

## 4.6 Dataset Construction

Provider-specific execution results were initially collected as separate datasets.

The resulting files included:

* Agentic_AI_Experiments_Main_OpenAI_V1.4.4_90Runs.xlsx
* Agentic_AI_Experiments_Main_Gemini_V1.4.4_90Runs.xlsx
* Agentic_AI_Experiments_Main_Claude_V1.4.4_90Runs.xlsx

Following completion of official data collection, provider datasets were merged into a unified dataset containing all experimental observations.

The merged dataset was subsequently processed to create an analysis-ready version suitable for statistical evaluation.

The primary analysis dataset consisted of:

* 270 observations
* 42 variables

and was stored as:

Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx

This dataset served as the frozen source for all statistical analyses reported in the study.

## 4.7 Data Validation

Dataset validation procedures were performed prior to statistical analysis.

Validation activities included verification of:

* Dataset completeness
* Variable consistency
* Provider allocation
* Workflow allocation
* Task metadata integrity
* Missing values in key outcome variables

The validation process confirmed that no missing values were present in the primary outcome variables:

* quality_score
* confidence
* cost_usd
* duration_sec
* total_tokens

Provider and workflow allocations were verified to be balanced according to the experimental design.

Validation results were documented within the study's statistical outputs and served as a prerequisite for subsequent descriptive statistics, assumption testing, analysis of variance procedures, and effect size estimation.

4.8 Experimental Control Measures

A primary objective of the experimental design was to maximize comparability across provider-workflow combinations. To achieve this objective, all controllable elements of the experimental environment were standardized.

The same benchmark tasks, workflow definitions, prompt templates, execution procedures, and evaluation criteria were applied throughout the study. Workflow Version V1.4.4 and Prompt Version frozen_v1.1 remained unchanged during official data collection. This approach reduced the likelihood that observed differences could be attributed to procedural variation rather than to the experimental variables under investigation.

The study also maintained a fixed benchmark task bank throughout execution. No tasks were added, removed, or modified after the start of official data collection. Consequently, all providers and workflow architectures were evaluated against identical task requirements.

These controls were intended to strengthen internal validity and improve confidence that observed performance differences reflected genuine variation between providers and workflow architectures.

4.9 Operational Monitoring and Execution Logging

All official executions were monitored and documented throughout data collection.

Execution records included workflow identifiers, provider information, task metadata, operational metrics, and execution outcomes. Retry events and operational anomalies were recorded separately to preserve transparency and facilitate later review of data collection procedures.

A small number of operational events were observed during experimentation. Google Gemini required four retry events, while Anthropic Claude required one retry event and generated one documented JSON compliance failure. These events were recorded within study logs and reviewed during dataset validation.

The maintenance of execution logs provided an auditable record of experimental activity and supported traceability between raw execution outputs and final analytical datasets. This documentation also improved transparency regarding the practical challenges associated with evaluating commercial foundation model APIs at scale.

4.10 Design Rationale

The experimental design was intended to balance methodological rigor with practical feasibility.

Three foundation model providers were selected to represent leading contemporary commercial large language model ecosystems. Evaluating multiple providers enabled assessment of whether workflow effects observed in prior work persisted across different foundation model implementations.

Three workflow architectures were selected because they represent increasing levels of agentic complexity while remaining directly comparable. The Basic Agent workflow provides a baseline condition, Planner–Executor introduces structured task decomposition, and Planner–Executor–Reviewer incorporates an additional review mechanism intended to improve output quality.

The benchmark consisted of 30 tasks distributed across Knowledge, Reasoning, and Coding categories. This scale was selected to provide meaningful task diversity while maintaining manageable experimental complexity. The resulting design generated 270 official executions, providing sufficient observations to support statistical comparison of providers, workflows, and interaction effects.

Collectively, these design decisions produced a controlled experimental framework capable of evaluating both performance outcomes and operational trade-offs across a representative set of contemporary agentic AI configurations.