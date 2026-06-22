# A Cross-Provider Evaluation of Agentic Workflow Architectures: Performance and Operational Trade-Offs in Foundation Model Systems

**Author:** Muawia Ali  
**Affiliation:** Independent Researcher  
**ORCID:** 0009-0000-2549-9862

**Keywords:** agentic AI; foundation model evaluation; workflow architecture; empirical software engineering; operational benchmarking; provider comparison; LLM evaluation validity

# Abstract

Foundation models are increasingly deployed inside agentic workflows that combine planning, execution, and review stages, but provider comparisons often evaluate models as standalone systems. This study presents a reproducible exploratory operational benchmark of provider × workflow configurations.

A balanced 3 × 3 factorial design compared OpenAI GPT-5.5, Google Gemini 2.5 Pro, and Anthropic Claude Sonnet 4.6 across Basic Agent, Planner–Executor, and Planner–Executor–Reviewer workflows. Thirty enterprise-oriented tasks spanning Knowledge, Reasoning, and Coding categories were executed using frozen prompts, fixed workflow logic, and a common task bank, producing 270 analysis-ready runs. Outcomes included a workflow-generated operational score (`quality_score`), model-reported confidence, estimated cost, duration, token consumption, and model call count.

The results indicate significant provider, workflow, and provider × workflow effects on the operational score. Task-blocked robustness analysis, which included task identity as a blocking factor, preserved the main pattern: workflow effects remained significant for the operational score, provider effects remained significant for confidence, and the provider × workflow interaction remained significant for the operational score. Planner–Executor achieved the highest mean operational score, while more complex reviewer workflows increased cost, duration, and token use.

A measurement-validity audit showed that `quality_score` equals confidence in non-reviewer workflows and mostly diverges in the reviewer workflow. The findings therefore support cautious system-level conclusions: provider and workflow should be evaluated jointly, and operational score differences should be interpreted as workflow-reported proxy evidence rather than independent human-rated quality.

# 1. Introduction

Foundation models and large language models are increasingly used as components of operational software and information systems. They support text generation, summarization, code production, decision support, and knowledge-work automation across enterprise settings. However, the behavior of such systems is not determined by the underlying model alone. In practical deployments, foundation models are embedded in workflow architectures that define how prompts are structured, whether tasks are decomposed, how intermediate plans are generated, and whether outputs are reviewed before delivery.

This shift from single-prompt usage to agentic workflow design creates a methodological and engineering challenge. A model evaluated in isolation may behave differently when embedded in a multi-stage workflow. Similarly, a workflow that improves outcomes for one provider may not produce the same benefit for another. As agentic AI systems become part of production environments, researchers and practitioners need evidence about complete provider × workflow configurations rather than provider rankings or workflow claims considered separately.

Agentic workflows introduce an architectural layer above the foundation model. A Basic Agent workflow submits the task directly to a model and returns a response. A Planner–Executor workflow separates task planning from response generation, allowing the system to organize a strategy before producing the answer. A Planner–Executor–Reviewer workflow adds a review stage intended to identify omissions, inconsistencies, or possible improvements. These architectures differ not only in reasoning structure but also in operational cost, execution duration, token consumption, and number of model calls.

From an empirical software engineering perspective, this makes workflow architecture a system-design variable. It can influence observed quality, reliability, and efficiency in ways that are not captured by model-level benchmarks alone. Enterprise AI evaluation therefore requires a broader operational benchmark: one that measures provider behavior, workflow architecture, and their interaction under controlled and reproducible conditions.

Prior work in this research program examined agentic workflow architectures using a single provider. That design was useful for identifying workflow-level differences, but it could not determine whether those differences generalize across foundation model providers. Contemporary providers differ in training procedures, instruction-following behavior, context handling, confidence calibration, and response-generation patterns. Consequently, a workflow effect observed under one provider may reflect either a general architectural pattern or an interaction with a specific model ecosystem.

The present study addresses this gap through Study 002, a controlled cross-provider operational benchmark of agentic workflow architectures. The study compares three foundation model providers—OpenAI GPT-5.5, Google Gemini 2.5 Pro, and Anthropic Claude Sonnet 4.6—across three workflow architectures: Basic Agent, Planner–Executor, and Planner–Executor–Reviewer. The evaluation uses a fixed 30-task bank, frozen prompt templates, Workflow Version V1.4.4, and standardized data collection procedures. The resulting dataset contains 270 official experimental runs, representing all provider × workflow × task combinations.

This paper treats `quality_score` as an operational workflow-generated quality proxy rather than an independent human judgment of answer quality. This distinction is important because the non-reviewer workflows do not include an independent reviewer stage. In those workflows, the parser can use confidence as the quality proxy when no separate quality score is emitted. In the Planner–Executor–Reviewer workflow, the reviewer stage can emit a distinct review-derived quality score. Accordingly, the study includes a measurement-validity audit and interprets all quality-related findings cautiously as system-level operational evidence.

The study investigates the following research questions:

- **RQ1:** How does workflow architecture affect operational quality scores in controlled agentic AI tasks?
- **RQ2:** How does foundation model provider affect confidence and operational performance?
- **RQ3:** Is there a provider × workflow interaction in quality and confidence outcomes?
- **RQ4:** What cost, latency, and token-consumption trade-offs arise as workflow complexity increases?

To answer these questions, the analysis combines descriptive statistics, two-way ANOVA, effect size estimation, measurement-validity auditing, robustness and sensitivity checks, task-stratified summaries, and operational-efficiency analysis. These analyses are intended to support a cautious but reproducible interpretation of how workflow design and provider selection jointly shape observed outcomes in agentic AI systems.

The results show that workflow architecture is associated with differences in the operational quality proxy, with the Planner–Executor workflow achieving the highest mean quality proxy across workflows. Provider selection is associated more strongly with confidence than with quality, and the significant provider × workflow interaction for quality indicates that workflow effectiveness is partly provider-dependent. Operational-efficiency analysis further shows that more complex workflows can increase cost, duration, and token use, so higher workflow complexity should not be assumed to produce better deployment value.

This paper makes five contributions. First, it provides a controlled cross-provider benchmark of agentic workflow architectures under fixed tasks, prompts, workflow versions, and data collection procedures. Second, it quantifies provider, workflow, and provider × workflow effects on operational quality and confidence outcomes. Third, it reports measurement-validity evidence showing where the operational quality proxy overlaps with or diverges from confidence. Fourth, it analyzes operational trade-offs involving cost, latency, token use, and workflow complexity. Fifth, it provides a reproducibility package containing the task bank, analysis-ready dataset, scripts, statistical outputs, publication tables, and publication figures used to support the manuscript results.

The remainder of the paper is organized as follows. Section 2 reviews related work on foundation model evaluation, agentic workflow architectures, evaluation validity, and operational AI systems. Section 3 presents the methodology. Section 4 details the experimental design. Section 5 describes the statistical analysis. Section 6 reports the results using the generated publication tables and figures. Section 7 discusses implications for agentic AI system design. Section 8 presents threats to validity. Section 9 describes the reproducibility package. Section 10 concludes the paper and outlines future work.

# 2. Related Work

## 2.1 Foundation Model Evaluation and Benchmarking

Foundation model evaluation has developed from narrow task accuracy measurement into a broader research area concerned with capability, robustness, fairness, transparency, and deployment relevance. HELM introduced a multidimensional evaluation framework intended to make language-model behavior more transparent across tasks, metrics, and scenarios [1]. MMLU provided an influential multi-domain benchmark for knowledge and reasoning assessment [2], while BIG-bench expanded the scale and diversity of capability testing across a wide range of language-model tasks [3]. More recent benchmarks have moved toward realistic operational settings. SWE-bench evaluates model performance on real software-engineering issues [4], and AgentBench evaluates language models as agents in interactive environments rather than as single-turn text generators [5].

These benchmark families demonstrate that model performance depends strongly on task design, evaluation protocol, and measurement assumptions. They also show a trend toward richer evaluation settings that better approximate practical deployment. However, most benchmark-oriented studies still evaluate the model as the primary unit of analysis. The workflow architecture surrounding the model is usually fixed, implicit, or treated as secondary. Study 002 extends this literature by treating provider and workflow as joint experimental factors and by reporting both effectiveness-oriented proxy metrics and operational metrics.

## 2.2 Evaluation Validity, LLM-as-Judge, and Confidence

Evaluation validity is a central challenge in foundation-model research. LLM-as-judge methods, such as MT-Bench and Chatbot Arena, have made scalable preference-oriented evaluation more practical, but they also introduce concerns such as position bias, verbosity bias, and dependence on the judging model [6], [7]. Related work on automated evaluators and debiasing methods further shows that measured quality can be sensitive to evaluator design and response length [8]. These concerns are directly relevant to studies that use model-generated or workflow-generated quality scores.

Confidence creates a related measurement problem. A model's expressed confidence is a self-assessment signal, not an externally verified estimate of correctness. For open-ended enterprise tasks, confidence may reflect provider-specific response style, calibration behavior, or instruction-following patterns. Therefore, confidence should be analyzed as a behavioral metric rather than as a direct substitute for answer quality. Study 002 follows this caution by interpreting `quality_score` as an operational workflow-generated proxy and by including a measurement-validity audit that identifies where quality and confidence overlap.

## 2.3 Agentic AI and Workflow Architectures

Agentic AI systems introduce a system-design layer above the foundation model. Surveys of LLM-based autonomous agents describe architectures that combine planning, memory, tool use, reflection, environmental interaction, and multi-step decision-making [9], [10]. Augmented-language-model research similarly frames language models as components that can be combined with tools, retrieval systems, external modules, and structured control logic [11]. Toolformer and related work demonstrate that language models can benefit from external tool interaction under appropriate conditions [12], while Generative Agents illustrates the use of memory, planning, and reflection in longer-running simulated agent behavior [13].

This literature establishes that agentic performance is not determined by model capability alone. A model's behavior can change when it is embedded in a workflow that decomposes tasks, introduces intermediate reasoning, or adds feedback stages. However, many agentic-workflow studies focus on one provider or one model family. As a result, the extent to which workflow effects generalize across providers remains underexplored. Study 002 addresses this gap by evaluating the same workflow architectures across three commercial provider ecosystems under frozen prompts and a common task bank.

## 2.4 Multi-Stage Reasoning, Review, and Self-Correction

Multi-stage reasoning research provides the conceptual basis for planner, executor, and reviewer architectures. Chain-of-Thought prompting showed that explicit intermediate reasoning can improve performance on complex reasoning tasks [14]. Self-consistency extended this idea by sampling multiple reasoning paths and selecting a consistent answer [15]. ReAct combined reasoning traces with action selection, supporting workflows that interleave thought and external action [16]. Tree of Thoughts introduced more deliberate exploration of reasoning trajectories before selecting a final solution [17].

Reflection and refinement methods provide more direct motivation for reviewer-style workflows. Reflexion introduced verbal reinforcement for language agents [18], and Self-Refine proposed iterative feedback and revision without additional model training [19]. However, recent critical work on self-correction shows that intrinsic self-correction is not uniformly reliable; it tends to work better when supported by reliable external feedback, tools, or task settings that make errors verifiable [20]. This is important for interpreting Study 002: the Planner–Executor–Reviewer workflow should not be assumed to improve performance merely because it adds a review stage. Its value must be measured empirically and weighed against operational overhead.

## 2.5 Cross-Provider Evaluation

Commercial foundation model ecosystems differ in training data, alignment methods, inference infrastructure, context handling, tool-use support, safety policies, and response style. Technical reports and independent benchmarks for GPT, Gemini, Claude, and related model families demonstrate rapid progress but also show that comparative results are sensitive to benchmark choice and model version [21]–[23]. Human-preference and benchmark leaderboards further indicate that no single model family should be treated as universally superior across all tasks and evaluation criteria.

Most cross-provider comparisons evaluate providers under a common prompt or benchmark but do not systematically vary the workflow architecture around each model. Conversely, many workflow studies examine architecture effects while holding the provider constant. This separation creates an evidence gap for deployed agentic systems, where the practical unit is not simply a model or a workflow but a provider × workflow configuration. Study 002 is positioned in this gap by testing whether workflow effects remain stable across providers and whether provider differences change under different workflow structures.

## 2.6 Operational Trade-Offs and Empirical Software Engineering Perspective

Operational metrics are increasingly important because agentic workflows can multiply model calls, tokens, latency, and cost. Research on efficient transformer inference and resource-aware language-model deployment highlights the practical importance of computational efficiency, not only model accuracy [24], [25]. Earlier work on energy and policy considerations for NLP also emphasized that model scale and computational demand have operational consequences [26], [27].

From an empirical software engineering perspective, workflow architecture can be treated as a system-design variable whose effects must be measured under controlled conditions. A workflow that improves a quality proxy may still be unattractive if it substantially increases latency, cost, or token consumption. Study 001 provided an initial single-provider evaluation of Basic Agent, Planner–Executor, and Planner–Executor–Reviewer architectures for enterprise-oriented tasks [28]. Study 002 extends that line of work by preserving the workflow definitions and task structure while introducing multiple providers, measurement-validity auditing, task-stratified summaries, robustness checks, and operational-efficiency analysis.

## 2.7 Research Gap and Positioning of Study 002

The reviewed literature establishes that foundation-model evaluation is mature, agentic workflows are an important design layer, multi-stage reasoning can improve outcomes under some conditions, provider differences are observable, and operational efficiency matters for deployment. However, three limitations remain. First, model benchmarks often evaluate providers without systematically varying workflow architecture. Second, workflow studies often evaluate architecture under a single provider. Third, operational trade-offs and measurement-validity issues are not always analyzed alongside provider × workflow effects.

Study 002 addresses these limitations through a controlled exploratory benchmark of three foundation model providers and three workflow architectures using identical tasks, frozen prompts, fixed workflow definitions, and a unified analysis pipeline. Its contribution is not a permanent provider ranking or an independent human-rated quality assessment. Instead, it provides reproducible system-level evidence about how provider selection and workflow architecture jointly shape operational quality proxies, confidence, cost, latency, token consumption, and efficiency trade-offs in agentic AI workflows.

# 3. Methodology

## 3.1 Study Objective and Positioning

The objective of Study 002 is to evaluate how foundation model provider and agentic workflow architecture are associated with operational outcomes in controlled AI workflow execution. The study is positioned as an exploratory operational benchmark rather than an independent human-rated assessment of answer quality. Its purpose is to provide reproducible system-level evidence about provider × workflow configurations, including quality-proxy behavior, confidence, cost, duration, token consumption, and workflow complexity.

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

In the reviewer workflow, the review stage received the task context and generated output and could emit a reviewer-derived `quality_score` together with review notes and a final answer. The stored `quality_score` for this workflow therefore reflects the workflow's internal reviewer output when available. For Basic Agent and Planner–Executor, no reviewer stage existed; consequently, when the parser did not receive an explicit quality score, it used model-reported confidence as the operational score. This parser behavior is the reason the manuscript treats `quality_score` as a workflow-reported operational proxy rather than as a measurement-equivalent quality construct across all workflows.

## 3.5 Foundation Model Providers

The study evaluated three commercially available foundation model providers:

- OpenAI GPT-5.5,
- Google Gemini 2.5 Pro,
- Anthropic Claude Sonnet 4.6.

These providers were selected because they represent widely used contemporary foundation model ecosystems and are relevant to enterprise AI deployment. The study does not claim universal provider superiority. Instead, provider findings are interpreted as time-bounded observations for the specific model versions, prompts, workflows, and task bank evaluated.

Official executions were collected between 2026-06-15T07:43:59Z and 2026-06-16T08:53:03Z. All rows in the frozen analysis dataset used Workflow Version V1.4.4, Prompt Version `frozen_v1.1`, and model temperature 1.0. The recorded model identifiers were `GPT-5.5`, `gemini-2.5-pro`, and `Claude Sonnet 4.6`.

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

Cost values were estimated from recorded input/output token estimates using the dataset pricing fields. The frozen dataset records the cost method as `estimated_char_count_all_llm_calls`, with input/output prices per one million tokens of 2.5/15.0 for OpenAI, 1.25/10.0 for Google, and 3.0/15.0 for Anthropic. These values support within-study operational comparison but should not be interpreted as permanent provider pricing.

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

The same analysis-ready dataset was also used to generate the publication assets reported in the Results section: `results/publication_tables_v2.md`, `results/publication_tables_v2.xlsx`, and the four publication figures under `results/figures_publication/`. These assets were treated as reporting outputs derived from the validated statistical pipeline, not as separate sources of evidence.

## 3.10 Reproducibility Strategy

Reproducibility was treated as a core design requirement. The study preserved the task bank, prompt version, workflow version, analysis-ready dataset, statistical scripts, generated workbooks, publication tables, and publication figures in a version-controlled research repository.

The reproducibility package includes scripts for dataset validation, descriptive statistics, assumption testing, ANOVA, effect size estimation, measurement-validity auditing, robustness and sensitivity analysis, operational-efficiency analysis, task-stratified analysis, and publication figure/table generation. This enables readers and reviewers to trace reported results from the analysis-ready dataset to final outputs.

Exact behavioral replication of commercial foundation models cannot be guaranteed because model providers may update deployed systems over time. However, preserving the evaluated prompts, workflow definitions, task bank, model identifiers, datasets, and analysis scripts provides a reproducible record of the experimental configuration and analytical process used in this study.

## 3.11 Scope of Inference

The study's findings apply to the evaluated provider versions, workflow definitions, prompt version, task bank, and execution period. The results should not be interpreted as permanent rankings of foundation model providers or as evidence that one workflow architecture is universally superior across settings. Instead, the study provides controlled operational evidence that workflow architecture and provider selection can interact, and that operational efficiency must be considered alongside quality-proxy and confidence outcomes when designing agentic AI systems.

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

The initial task-bank structure was selected during the Study 001 planning process using ChatGPT-assisted research design discussion. The accepted design used 30 tasks, balanced as 10 Knowledge tasks, 10 Reasoning tasks, and 10 Coding tasks. These categories were selected to represent common forms of enterprise AI work while providing diversity in cognitive and technical requirements.

Tasks were sourced from task_bank_v1 and remained unchanged throughout the study. The use of a frozen benchmark ensured that all providers and workflows were evaluated against identical task requirements.

The benchmark also retained secondary difficulty annotations:

* Easy
* Medium
* Hard

These labels were available in `task_bank_v1` before statistical analysis and were not modified after data collection. They are treated as secondary descriptive annotations because the primary benchmark design was balanced by task category rather than by difficulty.

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

This imbalance reflects the preserved task bank and is reported as a secondary descriptive characteristic rather than as a primary design feature.

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

## 4.8 Experimental Control Measures

A primary objective of the experimental design was to maximize comparability across provider-workflow combinations. To achieve this objective, all controllable elements of the experimental environment were standardized.

The same benchmark tasks, workflow definitions, prompt templates, execution procedures, and evaluation criteria were applied throughout the study. Workflow Version V1.4.4 and Prompt Version frozen_v1.1 remained unchanged during official data collection. This approach reduced the likelihood that observed differences could be attributed to procedural variation rather than to the experimental variables under investigation.

The study also maintained a fixed benchmark task bank throughout execution. No tasks were added, removed, or modified after the start of official data collection. Consequently, all providers and workflow architectures were evaluated against identical task requirements.

These controls were intended to strengthen internal validity and improve confidence that observed performance differences reflected genuine variation between providers and workflow architectures.

## 4.9 Operational Monitoring and Execution Logging

All official executions were monitored and documented throughout data collection.

Execution records included workflow identifiers, provider information, task metadata, operational metrics, and execution outcomes. Retry events and operational anomalies were recorded separately to preserve transparency and facilitate later review of data collection procedures.

A small number of operational events were observed during experimentation. Google Gemini required four retry events, while Anthropic Claude required one retry event and generated one documented JSON compliance failure. These events were recorded within study logs and reviewed during dataset validation.

The maintenance of execution logs provided an auditable record of experimental activity and supported traceability between raw execution outputs and final analytical datasets. This documentation also improved transparency regarding the practical challenges associated with evaluating commercial foundation model APIs at scale.

## 4.10 Design Rationale

The experimental design was intended to balance methodological rigor with practical feasibility.

Three foundation model providers were selected to represent leading contemporary commercial large language model ecosystems. Evaluating multiple providers enabled assessment of whether workflow effects observed in prior work persisted across different foundation model implementations.

Three workflow architectures were selected because they represent increasing levels of agentic complexity while remaining directly comparable. The Basic Agent workflow provides a baseline condition, Planner–Executor introduces structured task decomposition, and Planner–Executor–Reviewer incorporates an additional review mechanism intended to improve output quality.

The benchmark consisted of 30 tasks distributed across Knowledge, Reasoning, and Coding categories. This scale was selected to provide meaningful task diversity while maintaining manageable experimental complexity. The primary task-bank balance was category-based, with 10 tasks assigned to each of the three categories. Difficulty labels were added later as a secondary annotation layer and were not used as the primary balancing criterion. The resulting design generated a balanced set of 270 official executions, enabling exploratory comparison across provider × workflow conditions while retaining task-level limitations.

Collectively, these design decisions produced a controlled experimental framework capable of evaluating both performance outcomes and operational trade-offs across a representative set of contemporary agentic AI configurations.


This structure directly supports the publication tables and figures used in the manuscript: provider × workflow summaries, task-category summaries, cost–quality trade-off visualization, and operational-efficiency ranking. Difficulty annotations are reported only as secondary descriptive strata because the official design was balanced by task category rather than by difficulty.

# 5. Statistical Analysis

## 5.1 Analysis Objectives

The statistical analysis was designed to evaluate how foundation model provider and workflow architecture were associated with operational outcomes in Study 002. The analysis followed the balanced 3 × 3 factorial structure of the experiment, with provider and workflow as the two primary experimental factors. The analysis was not intended to produce permanent provider rankings or independent human-rated quality claims. Instead, it was designed to provide reproducible evidence about operational quality-proxy behavior, model-reported confidence, and deployment-relevant resource trade-offs.

The primary analytical objectives were:

- to quantify differences associated with foundation model provider;
- to quantify differences associated with workflow architecture;
- to evaluate provider × workflow interaction effects;
- to estimate effect magnitudes alongside statistical significance;
- to audit the relationship between `quality_score` and confidence;
- to examine robustness and sensitivity of descriptive patterns; and
- to connect statistical results with publication figures, publication tables, and operational-efficiency summaries.

The primary outcome variables were `quality_score`, interpreted as an operational workflow-generated quality proxy, and confidence, interpreted as model-reported self-assessment. Additional operational metrics included estimated cost, execution duration, total token consumption, and model call count.

## 5.2 Dataset Preparation

All analyses used the frozen analysis-ready dataset:

`Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx`

The dataset contained 270 validated observations from 30 benchmark tasks executed across three providers and three workflow architectures. Each provider × workflow cell contained 30 observations. The task bank was balanced by category, with 10 Knowledge, 10 Reasoning, and 10 Coding tasks. Difficulty labels were retained as secondary annotations rather than as the primary balancing criterion.

Before analysis, the dataset was checked for completeness, provider/workflow consistency, task coverage, and availability of the primary outcome and operational variables. Dataset validation outputs were preserved in `analysis/statistical_outputs/dataset_validation_report.xlsx`.

## 5.3 Descriptive Statistics

Descriptive statistics were generated before inferential testing to summarize central tendencies, dispersion, and operational trade-offs. These summaries included provider-level, workflow-level, provider × workflow, task-category, and difficulty-annotation views.

The publication reporting package uses these descriptive outputs in two forms. First, `results/publication_tables_v2.md` and `results/publication_tables_v2.xlsx` summarize provider × workflow outcomes, task-category outcomes, secondary difficulty annotations, and top operational-efficiency configurations. Second, the four publication figures in `results/figures_publication/` visualize mean quality by provider × workflow, quality by task category, cost–quality trade-offs, and operational-efficiency rankings.

## 5.4 Assumption Testing

Assumption testing was conducted for the primary outcomes before applying factorial ANOVA. The assessment included distributional checks and homogeneity-of-variance checks across experimental groups. Statistical outputs were preserved in `analysis/statistical_outputs/assumption_tests.xlsx` and `analysis/statistical_outputs/formal_assumption_tests.xlsx`.

The tests indicated that the data did not fully satisfy all parametric assumptions. Because the design was balanced with equal cell sizes, two-way ANOVA was retained as the primary inferential method, but results were interpreted alongside effect sizes, descriptive statistics, robustness and sensitivity checks, and measurement-validity evidence. This approach supports cautious interpretation rather than overreliance on p-values.

## 5.5 Two-Way ANOVA and Effect Sizes

Two-way ANOVA was used to estimate provider effects, workflow effects, and provider × workflow interaction effects for the primary outcomes. Separate models were used for the operational quality proxy and confidence. This framework aligned with the factorial experimental design and allowed the study to test whether workflow behavior differed across providers.

Effect size estimation was performed using partial eta squared (partial η²). Effect sizes were reported alongside F statistics and p-values to support practical interpretation of the observed effects. ANOVA outputs were preserved in `analysis/statistical_outputs/anova_results.xlsx`, and effect size outputs were preserved in `analysis/statistical_outputs/effect_sizes.xlsx`.

## 5.6 Task-Blocked Robustness Analysis

Because the same 30 benchmark tasks were executed under every provider × workflow condition, an additional task-blocked robustness analysis was conducted before final interpretation. This analysis included task identity as a blocking factor and compared nested fixed-effect models of the form `outcome ~ task block + provider + workflow + provider × workflow`.

The task-blocked analysis was not intended to replace the primary ANOVA outputs; rather, it tested whether the main conclusions remained visible after accounting for repeated task identity. For the operational score, workflow remained significant, F(2, 236) = 15.727, p < 0.001, partial η² = 0.118; provider remained significant, F(2, 236) = 3.496, p = 0.032, partial η² = 0.029; and the provider × workflow interaction remained significant, F(4, 232) = 5.522, p < 0.001, partial η² = 0.087. For confidence, provider remained significant, F(2, 236) = 13.256, p < 0.001, partial η² = 0.101; workflow remained significant, F(2, 236) = 3.935, p = 0.021, partial η² = 0.032; and the provider × workflow interaction was not significant at α = 0.05, F(4, 232) = 2.242, p = 0.065, partial η² = 0.037.

The task-blocked outputs are preserved in `analysis/statistical_outputs/task_blocked_analysis.xlsx` and summarized in `results/task_blocked_analysis_summary.md`. These results support the same cautious interpretation as the primary analysis: provider and workflow should be evaluated jointly, but effects on `quality_score` remain effects on an operational proxy whose construction differs between reviewer and non-reviewer workflows.

## 5.7 Measurement-Validity Audit

Because `quality_score` was generated by workflow outputs rather than by independent human raters, a measurement-validity audit was included as a required interpretive step. The audit examined where `quality_score` equaled confidence and where the two variables diverged across workflows, providers, and provider × workflow cells.

This audit was especially important because Basic Agent and Planner–Executor workflows did not include an independent reviewer stage. In those workflows, the parser could use confidence as the operational quality proxy when no separate quality score was emitted. In contrast, Planner–Executor–Reviewer included a review stage capable of emitting a distinct review-derived score. The audit output was preserved in `analysis/statistical_outputs/measurement_validity_audit.xlsx`.

## 5.8 Robustness, Sensitivity, and Task-Stratified Analyses

Robustness and sensitivity analyses were added to strengthen journal readiness without collecting new data. These checks included medians, interquartile ranges, deterministic bootstrap confidence intervals, trimmed means, IQR-based outlier sensitivity, reviewer versus non-reviewer comparisons, and simple mean-difference contrasts. They are reported as descriptive sensitivity evidence, not as replacements for independent human validation.

Task-stratified analyses summarized outcomes by the original task categories and by the secondary difficulty annotations. These outputs support transparent reporting of whether patterns were consistent across Knowledge, Reasoning, and Coding tasks while avoiding overclaims about difficulty-balanced design. Robustness and task-stratified outputs were preserved in `analysis/statistical_outputs/robustness_sensitivity.xlsx` and `analysis/statistical_outputs/task_stratified_analysis.xlsx`.

## 5.9 Operational-Efficiency Analysis

Operational-efficiency analysis examined how quality-proxy outcomes related to cost, duration, token consumption, and model call count. The analysis produced descriptive metrics such as quality per dollar, quality per 1,000 tokens, quality per second, and a balanced operational-efficiency index.

These efficiency outputs support the manuscript's practical contribution: workflow complexity must be evaluated against deployment constraints. The operational-efficiency workbook was preserved in `analysis/statistical_outputs/operational_efficiency.xlsx`, and the corresponding manuscript-facing summaries are reported in Table 4 and Figure 4.

## 5.10 Reporting and Reproducibility

All statistical outputs were generated from the frozen analysis-ready dataset and retained in the public repository. The analysis pipeline preserved dataset validation, descriptive statistics, assumption testing, ANOVA, effect sizes, measurement-validity auditing, robustness and sensitivity checks, task-stratified summaries, operational-efficiency analysis, publication tables, and publication figures.

The reporting strategy therefore links each manuscript claim to a reproducible artifact. Inferential claims are based on ANOVA and effect-size outputs, descriptive claims are based on generated tables and figures, and interpretive claims are bounded by the measurement-validity audit and threats-to-validity discussion.

# 6. Results

## 6.1 Dataset and Analysis Overview

The final Study 002 dataset contained 270 successful experimental runs from a balanced 3 × 3 factorial design: three foundation model providers, three workflow architectures, and 30 benchmark tasks. Each provider × workflow cell contained 30 observations. The task bank contained 10 Knowledge, 10 Reasoning, and 10 Coding tasks. Difficulty labels were available as secondary annotations and were not the primary balancing criterion.

All primary analytical variables were available in the analysis-ready dataset, including the operational score (`quality_score`), confidence, estimated cost, execution duration, total token consumption, and model call count. Table 1 reports provider × workflow descriptive summaries; Table 2 reports task-category summaries; Table 3 reports secondary difficulty annotations; and Table 4 reports operational-efficiency rankings. Figures 1–4 visualize the corresponding provider × workflow quality heatmap, task-category quality pattern, cost–quality trade-off, and operational-efficiency ranking.

**Table 1. Provider × workflow descriptive summary.** Unit of analysis is one successful task execution; N = 30 for each provider × workflow cell. `quality_score` is interpreted as a workflow-reported operational score.

- OpenAI / Basic Agent: mean score = 0.940; SD = 0.030; mean cost = $0.0055; duration = 8.333 s; tokens = 448.0.
- OpenAI / Planner–Executor: mean score = 0.939; SD = 0.026; mean cost = $0.0107; duration = 15.047 s; tokens = 1047.0.
- OpenAI / Planner–Executor–Reviewer: mean score = 0.895; SD = 0.031; mean cost = $0.0206; duration = 26.613 s; tokens = 2265.3.
- Google / Basic Agent: mean score = 0.903; SD = 0.246; mean cost = $0.0027; duration = 11.560 s; tokens = 360.6.
- Google / Planner–Executor: mean score = 0.993; SD = 0.022; mean cost = $0.0072; duration = 22.547 s; tokens = 1085.4.
- Google / Planner–Executor–Reviewer: mean score = 0.732; SD = 0.314; mean cost = $0.0144; duration = 47.280 s; tokens = 2434.4.
- Anthropic / Basic Agent: mean score = 0.874; SD = 0.170; mean cost = $0.0065; duration = 9.897 s; tokens = 510.7.
- Anthropic / Planner–Executor: mean score = 0.901; SD = 0.102; mean cost = $0.0109; duration = 15.613 s; tokens = 1045.5.
- Anthropic / Planner–Executor–Reviewer: mean score = 0.841; SD = 0.132; mean cost = $0.0210; duration = 25.620 s; tokens = 2262.8.

## 6.2 RQ1: Workflow Effects on the Operational Quality Proxy

Workflow architecture was significantly associated with the operational quality proxy, F = 14.329, p < 0.001, partial η² = 0.099. This was the largest main effect observed for quality and is interpreted as a medium effect. Provider selection also had a statistically significant but smaller effect, F = 3.186, p = 0.043, partial η² = 0.024.

Across workflows, Planner–Executor achieved the highest mean quality proxy (M = 0.944), followed by Basic Agent (M = 0.905) and Planner–Executor–Reviewer (M = 0.822). Table 1 and Figure 1 (`figure_01_quality_heatmap_provider_workflow.png`) summarize mean quality by provider × workflow condition. These results indicate that adding a planning stage was associated with stronger operational quality-proxy outcomes in this benchmark, but adding a reviewer stage did not uniformly improve the proxy metric.

## 6.3 RQ2: Provider Effects on Confidence and Operational Outcomes

Provider selection was more strongly associated with confidence than with the operational quality proxy. For confidence, provider had a significant medium effect, F = 12.209, p < 0.001, partial η² = 0.086. Workflow architecture also had a statistically significant but smaller effect on confidence, F = 3.624, p = 0.028, partial η² = 0.027.

Mean confidence differed across providers, with Google showing the highest mean confidence (M = 0.964), followed by OpenAI (M = 0.942) and Anthropic (M = 0.886). Because confidence is model-reported, these findings should be interpreted as differences in provider self-assessment behavior rather than externally verified correctness.

## 6.4 RQ3: Provider × Workflow Interaction

The provider × workflow interaction was significant for the operational quality proxy, F = 4.673, p = 0.001, partial η² = 0.067. This medium interaction effect indicates that workflow behavior differed across providers. For example, Google achieved a high mean quality proxy under Planner–Executor but a lower mean under Planner–Executor–Reviewer, while OpenAI showed more stable quality-proxy behavior across workflow conditions.

For confidence, the provider × workflow interaction was not statistically significant, F = 2.022, p = 0.092, partial η² = 0.030. This contrast suggests that workflow-provider interactions were more visible in the operational score than in confidence.

The task-blocked robustness analysis preserved this pattern after including task identity as a blocking factor. For the operational score, provider, workflow, and provider × workflow effects remained statistically significant. For confidence, provider and workflow remained significant, while the provider × workflow interaction remained non-significant at α = 0.05. This supports the interpretation that the main patterns are not solely an artifact of pooling repeated task observations, although the design remains exploratory and bounded by the operational-score construct.

## 6.5 Measurement-Validity Audit

The measurement-validity audit showed that `quality_score` and confidence were identical for all Basic Agent observations and all Planner–Executor observations. In contrast, they were mostly distinct in the Planner–Executor–Reviewer workflow: only 5 of 90 reviewer-workflow observations (5.6%) had identical quality and confidence values.

This finding is central to interpretation. For non-reviewer workflows, the operational quality proxy overlaps with confidence when no independent quality score is emitted. For the reviewer workflow, the review stage can produce a distinct score. Therefore, quality-related results in this study should be read as operational workflow-generated proxy evidence, not as independent human-rated answer quality.

## 6.6 Robustness, Task-Stratified, and Efficiency Findings

Robustness outputs supported cautious interpretation of the main descriptive pattern. Median quality was 0.950 for Basic Agent, 0.950 for Planner–Executor, and 0.880 for Planner–Executor–Reviewer. Bootstrap and outlier-sensitivity outputs were generated to document stability without treating them as replacements for independent validation.

Task-stratified analysis showed category-level variation. Mean operational score was highest for Knowledge tasks (M = 0.919), followed by Reasoning tasks (M = 0.900) and Coding tasks (M = 0.853). Table 2 and Figure 2 (`figure_02_quality_by_task_category.png`) summarize these category-level results.

**Table 2. Task-category summary.** Knowledge tasks had N = 90, mean score = 0.919, SD = 0.092, and mean confidence = 0.943. Reasoning tasks had N = 90, mean score = 0.900, SD = 0.145, and mean confidence = 0.941. Coding tasks had N = 90, mean score = 0.853, SD = 0.233, and mean confidence = 0.907.

Table 3 reports difficulty-annotation summaries; these are exploratory because difficulty was a secondary annotation layer rather than a balancing criterion. Easy tasks had N = 63 and mean score = 0.884; medium tasks had N = 99 and mean score = 0.900; hard tasks had N = 108 and mean score = 0.886.

Operational-efficiency analysis showed that workflow complexity increased resource requirements. Basic Agent had the lowest mean model-call count (1.0), Planner–Executor averaged 2.0 calls, and Planner–Executor–Reviewer averaged 3.0 calls. Figure 3 (`figure_03_cost_quality_tradeoff.png`) presents the cost–score trade-off, while Table 4 and Figure 4 (`figure_04_operational_efficiency_ranking.png`) summarize the top configurations by a descriptive balanced-efficiency index.

**Table 4. Operational-efficiency ranking.** The highest descriptive balanced-efficiency configurations were Google / Basic Agent (index = 0.805), OpenAI / Basic Agent (0.669), Anthropic / Basic Agent (0.531), Google / Planner–Executor (0.360), and OpenAI / Planner–Executor (0.329). These rankings are deployment-oriented summaries, not universal recommendations.

**Figure 1. Mean operational score by provider × workflow.** This heatmap summarizes the provider × workflow pattern for the workflow-reported operational score.

**Figure 2. Mean operational score by task category.** This figure summarizes Knowledge, Reasoning, and Coding category-level patterns.

**Figure 3. Cost–score trade-off by provider × workflow.** This plot compares mean estimated cost against mean operational score for each configuration.

**Figure 4. Operational-efficiency ranking.** This chart summarizes the descriptive balanced-efficiency index for provider × workflow configurations.

These results indicate that workflow selection involves practical trade-offs among operational score, cost, latency, token usage, and model calls.

# 7. Discussion

Study 002 evaluated agentic AI systems as provider × workflow configurations rather than as standalone foundation models. This framing is important because practical deployments rarely use a model in isolation. They embed the model in processes that structure planning, execution, review, and output handling. The results show that both provider selection and workflow architecture matter, but their influence differs by outcome.

## 7.1 Workflow Architecture as a System-Design Variable

The strongest quality-related main effect was associated with workflow architecture. Planner–Executor achieved the highest mean operational quality proxy, while the more complex Planner–Executor–Reviewer workflow did not produce uniformly stronger results. This suggests that workflow engineering can materially affect observed system behavior, but greater workflow complexity is not automatically beneficial.

From an empirical software engineering perspective, this supports treating workflow architecture as a design variable that requires evaluation, not as a neutral wrapper around a foundation model. Planning may help structure task execution, but review stages can introduce additional variability, cost, or scoring behavior depending on how they are implemented and how the underlying model responds to them.

## 7.2 Provider and Workflow Should Be Evaluated Jointly

The significant provider × workflow interaction for the operational quality proxy indicates that workflow effects were provider-dependent. This finding cautions against evaluating workflows with one model and assuming the same pattern will transfer to other providers. It also cautions against model comparisons that ignore the workflow context in which the model will be deployed.

For practice, the implication is straightforward: organizations should benchmark complete workflow-provider combinations. A provider that performs well in a direct Basic Agent setting may not be optimal under a multi-stage architecture, and a workflow that improves one provider may not improve another. This supports a co-design view of agentic AI systems in which model capability, workflow structure, operational constraints, and evaluation criteria are selected together.

## 7.3 Confidence Is Not Equivalent to Quality

The confidence results differed from the quality-proxy results. Provider selection had the strongest effect on confidence, while workflow had a smaller effect, and the provider × workflow interaction was not statistically significant. This pattern suggests that confidence reflects provider-specific self-assessment behavior as much as task outcome.

The measurement-validity audit further strengthens this caution. In non-reviewer workflows, `quality_score` overlapped fully with confidence because no independent reviewer stage was available. In the reviewer workflow, quality and confidence mostly diverged. Therefore, confidence should not be treated as a direct substitute for externally verified quality, and `quality_score` should be reported as an operational proxy rather than as human-rated correctness.

## 7.4 Operational Efficiency Is a Core Contribution

The operational results show that workflow sophistication has measurable deployment costs. Planner–Executor–Reviewer required additional model calls, tokens, duration, and cost. Although multi-stage workflows can improve structure and sometimes improve quality-proxy outcomes, those benefits must be evaluated against latency and cost constraints.

This is especially relevant for enterprise settings. A system that produces slightly stronger outputs may be less useful if it is slower, more expensive, or harder to scale. The cost–quality and efficiency-ranking figures therefore provide practical evidence for selecting workflows under operational constraints, not merely under quality-oriented benchmarks.

In the publication assets, Figure 3 makes this trade-off visible by placing mean quality proxy against mean cost, while Figure 4 and Table 4 summarize descriptive balanced-efficiency rankings. These outputs should be read as deployment-oriented decision aids, not as universal rankings, because organizations may weight cost, latency, quality proxy, and reliability differently.

## 7.5 Implications for Research and Deployment

For researchers, the study shows the value of reporting provider × workflow interactions, measurement-validity audits, and operational metrics alongside primary performance results. For practitioners, it suggests that deployment decisions should not be based on provider reputation or workflow complexity alone. Instead, teams should evaluate the specific configuration they intend to use, using metrics that reflect both output behavior and operational feasibility.

The study also highlights the need for stronger follow-up evaluation. Future work should add independent human ratings, inter-rater reliability, task-specific rubrics, additional providers, open-source models, and additional workflow architectures such as retrieval-augmented, tool-using, reflection-based, and multi-agent designs. Such work would extend the present operational benchmark into a more comprehensive evaluation of agentic AI system quality.

# 8. Threats to Validity

This study used a controlled and reproducible experimental design, including frozen prompts, fixed workflow definitions, a common task bank, and balanced provider × workflow execution. Nevertheless, the findings should be interpreted within several validity boundaries.

## 8.1 Internal Validity

Internal validity concerns whether observed differences can reasonably be attributed to the experimental factors rather than uncontrolled variation. The study strengthened internal validity by holding task definitions, prompt version, workflow version, execution procedure, and primary analysis pipeline constant across providers. Each provider × workflow cell contained 30 observations, producing a balanced design for the main experimental factors.

Some sources of internal variation remain. Commercial foundation model providers operate proprietary inference systems that may include undisclosed routing, load balancing, safety policies, or inference optimizations. These factors may influence outputs independently of the workflow and provider labels available to the researcher. In addition, large language model outputs may vary across repeated executions even with the same prompt and workflow configuration.

A small number of operational anomalies were documented during data collection, including retry events and one JSON compliance issue. These events were recorded and managed through the study protocol, and the final analysis-ready dataset contained 270 successful runs. However, such events illustrate that evaluations of commercial foundation model APIs may be affected by transient service behavior.

## 8.2 Construct and Measurement Validity

Construct validity is the most important limitation of this study. The variable `quality_score` is not interpreted as an independent human judgment of answer quality. It is an operational workflow-generated quality proxy extracted from the workflow execution schema.

The measurement-validity audit showed that `quality_score` was identical to confidence for all Basic Agent and Planner–Executor observations. This occurred because those workflows did not include an independent reviewer stage, and the parser used confidence as the quality proxy when no separate quality score was emitted. In the Planner–Executor–Reviewer workflow, quality and confidence were mostly distinct because the reviewer stage could emit a review-derived score.

As a result, quality-related conclusions should be interpreted cautiously. The study provides reproducible operational evidence about workflow-generated metrics, not an independent assessment of human-perceived answer quality. Confidence also has construct limitations because it represents model-reported self-assessment rather than externally calibrated certainty. Future work should add independent human raters, inter-rater reliability, and a multi-dimensional scoring rubric covering factual accuracy, completeness, reasoning quality, usefulness, and safety.

Operational metrics also have scope limits. Estimated cost, duration, and token use are important deployment indicators, but they do not capture every practical factor, such as rate limits, integration complexity, infrastructure overhead, availability guarantees, or organizational compliance requirements.

## 8.3 External Validity

External validity concerns whether the findings generalize beyond the evaluated setting. The study examined three providers, three workflow architectures, one prompt version, one workflow version, and a 30-task enterprise-oriented benchmark. These choices provide useful coverage but do not represent all possible agentic AI systems.

The task bank was balanced by category, with 10 Knowledge, 10 Reasoning, and 10 Coding tasks. Difficulty labels were added later as a secondary annotation layer and were not used as the primary balancing criterion. Therefore, difficulty-stratified findings should be interpreted as exploratory rather than as evidence from a difficulty-balanced benchmark.

The results should not be interpreted as permanent provider rankings or universal workflow recommendations. Different task domains, model versions, prompts, tool integrations, retrieval mechanisms, memory systems, or multi-agent coordination patterns may produce different outcomes. Domains such as healthcare, finance, law, cybersecurity, software maintenance, and scientific research may also require different evaluation rubrics and risk controls.

## 8.4 Statistical Conclusion Validity

The balanced factorial design supports comparison across provider and workflow conditions, but statistical conclusions remain bounded by sample size and metric properties. The main design contained 30 tasks repeated across each provider × workflow cell, yielding 270 observations. This is sufficient for an exploratory operational benchmark but does not eliminate uncertainty around subgroup analyses.

Assumption testing indicated that the data did not fully satisfy all parametric assumptions. For this reason, the study reports effect sizes, robustness and sensitivity analyses, medians, interquartile ranges, bootstrap confidence intervals, outlier checks, reviewer versus non-reviewer comparisons, and task-stratified summaries. These analyses support cautious interpretation but do not replace independent validation using human-rated outcomes.

The operational-efficiency index is descriptive. It normalizes observed quality-proxy behavior against cost, duration, and token use, but it should not be interpreted as a context-free ranking rule. Different deployment contexts may weight cost, latency, quality, and reliability differently.

The publication tables and figures inherit the same limitations. They summarize the validated dataset and improve reporting clarity, but they do not transform workflow-generated proxies into human-rated quality evidence or make the efficiency index a context-independent optimization target.

## 8.5 Reproducibility and Temporal Validity

Reproducibility is challenging in research involving commercial foundation models because providers can update model behavior, pricing, safety layers, inference infrastructure, and API behavior without full public visibility. The study mitigates this by preserving the task bank, prompts, workflow version, model identifiers, analysis-ready dataset, scripts, statistical outputs, publication tables, and figures in a version-controlled repository.

Even with these materials, exact behavioral replication may not be possible if providers change the evaluated systems. The findings should therefore be interpreted as a time-bounded record of the evaluated provider × workflow configurations under the study's execution conditions. This limitation is inherent to empirical research on rapidly evolving foundation model systems and motivates repeated benchmark updates over time.

## 8.6 Summary

The study provides controlled operational evidence about agentic AI workflow configurations, but its conclusions are bounded by the use of an operational quality proxy, absence of independent human ratings, the selected task bank, commercial model drift, and the evaluated workflow/provider set. These limitations do not invalidate the benchmark; rather, they define its proper interpretation as a reproducible exploratory study and motivate follow-up work with independent quality assessment and broader workflow coverage.

# 9. Reproducibility Package

Reproducibility represents an important challenge in contemporary foundation model research due to the rapid evolution of commercial AI systems, provider-side model updates, and differences in experimental implementation. To improve transparency and facilitate future verification efforts, Study 002 was designed with reproducibility as a core methodological objective.

The study preserved workflow definitions, prompt templates, benchmark tasks, datasets, analytical outputs, and publication assets within a version-controlled research repository. This approach provides traceability from raw experimental executions to the final results reported in the manuscript and enables independent examination of the experimental process.

## 9.1 Repository Structure

All study materials were maintained within the Study 002 research directory:

```text
research/study_002_foundation_model_comparison/
```

The repository includes dedicated folders for datasets, workflow definitions, statistical analysis, publication assets, and manuscript preparation.

Key components include:

* Provider-specific datasets
* Merged datasets
* Benchmark task bank
* Execution logs
* Workflow definitions
* Analysis scripts
* Statistical outputs
* Publication tables
* Publication figures
* Manuscript materials

This structure was intended to separate data collection, analysis, reporting, and documentation activities while preserving traceability across all stages of the research process.

## 9.2 Version-Controlled Experimental Assets

To minimize procedural drift during experimentation, all major experimental assets were frozen prior to official data collection.

The study used:

* Workflow Version V1.4.4
* Prompt Version frozen_v1.1
* task_bank_v1

These assets remained unchanged throughout the official experimental phase.

Version control was maintained through Git-based repository management. Experimental milestones, data collection phases, statistical analyses, and manuscript development activities were documented through commits and tagged releases. This process provides a documented history of project evolution and supports independent review of the research workflow.

## 9.3 Datasets and Data Preservation

Provider-specific results were preserved as separate datasets for OpenAI, Google Gemini, and Anthropic Claude. These datasets were subsequently merged into a unified experimental dataset and an analysis-ready dataset used for statistical evaluation.

The primary frozen dataset used throughout the analytical phase was:

Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx

This dataset contains 270 validated observations and served as the source for all descriptive statistics, assumption tests, inferential analyses, effect size calculations, tables, and figures reported in the study.

Maintaining a frozen analysis dataset reduces the possibility of inadvertent modifications during later analytical stages and supports consistent replication of reported findings.

## 9.4 Analytical Reproducibility

All major analytical procedures were preserved through dedicated analysis scripts and documented output files.

The analytical workflow included:

* Dataset validation
* Descriptive statistics
* Assumption testing
* Formal assumption testing
* Analysis of variance
* Effect size estimation
* Measurement-validity auditing
* Robustness and sensitivity analysis
* Task-stratified analysis
* Operational-efficiency analysis

Supporting scripts were retained within:

```text
analysis/scripts/
```

while generated outputs were preserved within:

```text
analysis/statistical_outputs/
```

This approach improves transparency by allowing analytical outputs to be traced back to specific processing steps and statistical procedures.

## 9.5 Publication Assets

Publication-oriented assets were generated directly from the validated analysis dataset and preserved separately from intermediate analytical outputs.

The repository includes:

* Publication tables
* Publication figures
* Statistical summaries

Final manuscript-facing publication figures were maintained within:

```text
results/figures_publication/
```

while publication tables were preserved as both spreadsheet and Markdown summaries:

```text
results/publication_tables_v2.xlsx
results/publication_tables_v2.md
```

Separating publication assets from intermediate analytical work reduces the likelihood of inconsistencies between reported findings and underlying statistical results.

The four current publication figures report: (1) mean operational quality proxy by provider × workflow, (2) quality proxy by task category, (3) cost–quality trade-off by provider × workflow, and (4) operational-efficiency ranking. These files are reporting artifacts generated from the validated dataset and should be interpreted using the measurement-validity limitations described in the manuscript.

## 9.6 Execution Logging and Traceability

Operational transparency was supported through structured execution logging.

Execution logs documented workflow executions, retry events, operational anomalies, and collection activities. These records provided an auditable history of data collection and enabled verification of execution outcomes during dataset validation.

Documented operational events included retry activity associated with Google Gemini executions and a JSON compliance failure observed during Anthropic Claude experimentation. These events were preserved within study logs and incorporated into validation procedures.

The retention of execution records improves transparency regarding the practical realities of large-scale evaluations involving commercial foundation model APIs.

## 9.7 Reproducibility Limitations

Despite extensive documentation and preservation efforts, exact replication of foundation model behavior cannot be guaranteed.

Commercial providers may introduce model updates, inference optimizations, pricing changes, or infrastructure modifications that alter system behavior over time. Consequently, future replications conducted using nominally identical workflows and prompts may not reproduce identical outputs.

This limitation reflects a broader challenge in empirical foundation model research rather than a limitation unique to the present study.

Accordingly, the reproducibility package should be interpreted as preserving the experimental procedures, datasets, analytical methods, and reporting pipeline associated with the evaluated systems at the time of experimentation.

## 9.8 Summary

The Study 002 reproducibility package was designed to support transparency, traceability, and independent verification. Through version-controlled workflows, frozen prompts, preserved benchmark tasks, validated datasets, documented analytical procedures, execution logs, and publication assets, the study provides a comprehensive record of the experimental and analytical process.

These materials strengthen confidence in the reported findings and support future replication, extension, and comparative research involving agentic workflow architectures and foundation model providers.

# 10. Conclusion

This study presented a controlled exploratory operational benchmark of agentic AI workflow configurations across three foundation model providers and three workflow architectures. Using a balanced 3 × 3 design, the study compared OpenAI GPT-5.5, Google Gemini 2.5 Pro, and Anthropic Claude Sonnet 4.6 across Basic Agent, Planner–Executor, and Planner–Executor–Reviewer workflows on a fixed 30-task enterprise-oriented benchmark.

The results indicate that workflow architecture is associated with meaningful differences in the operational quality proxy, while provider selection is more strongly associated with model-reported confidence. The significant provider × workflow interaction for the quality proxy suggests that workflow behavior should not be assumed to transfer uniformly across providers. In practical terms, model selection and workflow design should be evaluated jointly rather than treated as independent decisions.

The study also shows that higher workflow complexity is not automatically equivalent to better deployment value. Planner–Executor achieved the highest mean operational quality proxy in this benchmark, while Planner–Executor–Reviewer increased cost, latency, token consumption, and model-call requirements without uniformly improving the quality proxy. The publication tables and figures make these trade-offs visible by summarizing provider × workflow outcomes, task-category patterns, cost–quality behavior, and operational-efficiency rankings.

A central limitation is that `quality_score` is an operational workflow-generated proxy rather than an independent human judgment of answer quality. The measurement-validity audit showed that the proxy overlapped with confidence in non-reviewer workflows and diverged mostly in the reviewer workflow. Therefore, the findings should be interpreted as reproducible system-level operational evidence, not as final claims about human-perceived answer quality or durable provider ranking.

The study contributes to research on agentic AI evaluation by showing how provider choice, workflow architecture, measurement validity, and operational efficiency can be analyzed within a single reproducible benchmark. It also provides a public reproducibility package containing the task bank, frozen prompts, workflow definitions, analysis-ready dataset, analysis scripts, statistical outputs, publication tables, and publication figures.

Future work should extend this benchmark with independent human ratings, inter-rater reliability, task-specific scoring rubrics, additional providers, open-source models, domain-specific task banks, retrieval-augmented workflows, tool-using workflows, and multi-agent coordination patterns. Repeated benchmark updates will also be necessary because commercial foundation model behavior, pricing, and infrastructure change over time.

Overall, Study 002 supports a cautious but practically important conclusion: agentic AI systems should be evaluated as complete provider × workflow configurations. For both researchers and practitioners, the relevant question is not only which model performs well, but which model-workflow combination provides acceptable quality-proxy behavior under the cost, latency, reproducibility, and validity constraints of the intended use case.

# References

[1] P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga, Y. Zhang, D. Narayanan, Y. Wu, A. Kumar, et al., “Holistic Evaluation of Language Models,” *Transactions on Machine Learning Research*, 2023.

[2] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt, “Measuring Massive Multitask Language Understanding,” in *International Conference on Learning Representations*, 2021.

[3] A. Srivastava, A. Rastogi, A. Rao, A. A. M. Shoeb, A. Abid, A. Fisch, A. R. Brown, A. Santoro, A. Gupta, A. Garriga-Alonso, et al., “Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models,” arXiv:2206.04615, 2022.

[4] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan, “SWE-bench: Can Language Models Resolve Real-World GitHub Issues?” in *International Conference on Learning Representations*, 2024.

[5] X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, et al., “AgentBench: Evaluating LLMs as Agents,” in *International Conference on Learning Representations*, 2024.

[6] L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica, “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena,” arXiv:2306.05685, 2023.

[7] W.-L. Chiang, L. Zheng, Y. Sheng, A. N. Angelopoulos, T. Li, D. Li, H. Zhang, B. Zhu, M. I. Jordan, J. E. Gonzalez, and I. Stoica, “Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference,” in *Proceedings of Machine Learning Research*, 2024.

[8] Y. Dubois, B. Galambosi, P. Liang, and T. B. Hashimoto, “Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators,” arXiv:2404.04475, 2024.

[9] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, W. X. Zhao, Z. Wei, and J.-R. Wen, “A Survey on Large Language Model Based Autonomous Agents,” *Frontiers of Computer Science*, 2024.

[10] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. Zhang, J. Wang, S. Jin, E. Zhou, et al., “The Rise and Potential of Large Language Model Based Agents: A Survey,” arXiv:2309.07864, 2023.

[11] G. Mialon, R. Dessì, M. Lomeli, M. Nalmpantis, R. Pasunuru, R. Raileanu, B. Rozière, T. Schick, J. Dwivedi-Yu, A. Celikyilmaz, A. Grave, Y. LeCun, and T. Scialom, “Augmented Language Models: A Survey,” *Transactions on Machine Learning Research*, 2023.

[12] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, M. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom, “Toolformer: Language Models Can Teach Themselves to Use Tools,” in *Advances in Neural Information Processing Systems*, 2023.

[13] J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein, “Generative Agents: Interactive Simulacra of Human Behavior,” in *ACM Symposium on User Interface Software and Technology*, 2023, doi: 10.1145/3586183.3606763.

[14] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. V. Le, and D. Zhou, “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models,” in *Advances in Neural Information Processing Systems*, 2022.

[15] X. Wang, J. Wei, D. Schuurmans, Q. V. Le, E. H. Chi, S. Narang, A. Chowdhery, and D. Zhou, “Self-Consistency Improves Chain of Thought Reasoning in Language Models,” in *International Conference on Learning Representations*, 2023.

[16] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, “ReAct: Synergizing Reasoning and Acting in Language Models,” in *International Conference on Learning Representations*, 2023.

[17] S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, and K. Narasimhan, “Tree of Thoughts: Deliberate Problem Solving with Large Language Models,” arXiv:2305.10601, 2023.

[18] N. Shinn, F. Cassano, E. Berman, A. Gopinath, K. Narasimhan, and S. Yao, “Reflexion: Language Agents with Verbal Reinforcement Learning,” in *Advances in Neural Information Processing Systems*, 2023.

[19] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al., “Self-Refine: Iterative Refinement with Self-Feedback,” in *Advances in Neural Information Processing Systems*, 2023.

[20] R. Kamoi, T. Goyal, J. D. Rodriguez, G. Durrett, and S. Doddapaneni, “When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs,” *Transactions of the Association for Computational Linguistics*, 2024, doi: 10.1162/tacl_a_00713.

[21] OpenAI, “GPT-4 Technical Report,” arXiv:2303.08774, 2023.

[22] Google Gemini Team, “Gemini: A Family of Highly Capable Multimodal Models,” arXiv:2312.11805, 2023.

[23] Anthropic, “The Claude 3 Model Family: Opus, Sonnet, Haiku,” Technical report / model card, 2024.

[24] R. Pope, S. Douglas, A. Chowdhery, J. Devlin, J. Bradbury, J. Heek, K. Xiao, S. Agrawal, and J. Dean, “Efficiently Scaling Transformer Inference,” in *Proceedings of Machine Learning and Systems*, 2023.

[25] Z. Wan, X. Wang, C. Liu, S. Alam, Y. Zheng, J. Liu, Z. Qu, S. Yan, Y. Zhu, Q. Zhang, M. Chowdhury, and M. Zhang, “Efficient Large Language Models: A Survey,” arXiv preprint, 2023.

[26] E. Strubell, A. Ganesh, and A. McCallum, “Energy and Policy Considerations for Deep Learning in NLP,” in *Proceedings of the Association for Computational Linguistics*, 2019, doi: 10.18653/v1/P19-1355.

[27] D. Patterson, J. Gonzalez, Q. Le, C. Liang, L.-M. Munguia, D. Rothchild, D. So, M. Texier, and J. Dean, “Carbon Emissions and Large Neural Network Training,” arXiv:2104.10350, 2021.

[28] M. Ali, “Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n,” Zenodo, 2026, doi: 10.5281/zenodo.20606084.
