# 3. Methodology

## 3.1 Research Objective

The objective of this study was to evaluate the relative influence of foundation model provider and workflow architecture on the performance of agentic AI systems. Specifically, the study sought to determine whether differences in answer quality, confidence, and operational performance were primarily attributable to the underlying foundation model or to the workflow architecture through which the model was deployed.

The study extends previous work that examined workflow architectures using a single foundation model provider. By introducing multiple providers while preserving workflow structure, prompts, tasks, and evaluation procedures, the present research isolates the effects of provider selection and workflow design under controlled conditions.

## 3.2 Experimental Approach

A controlled experimental methodology was adopted to enable direct comparison of workflow architectures across multiple foundation model providers.

The experimental design was based on the principle of isolating independent variables while maintaining all other conditions constant. Workflow logic, prompt templates, task definitions, execution procedures, and evaluation criteria were standardized across providers. This approach reduced potential confounding factors and improved comparability between experimental conditions.

The study employed a comparative evaluation framework in which multiple workflow architectures were executed against a common benchmark task set. Performance outcomes were subsequently analyzed using quantitative statistical methods.

## 3.3 Agentic Workflow Architectures

Three workflow architectures were evaluated.

### Basic Agent

The Basic Agent architecture represents a single-agent execution model in which a task is presented directly to a foundation model and a response is generated without explicit planning or review stages.

This architecture serves as the baseline condition against which more sophisticated workflows are compared.

### Planner–Executor

The Planner–Executor architecture separates planning and execution into distinct stages. An initial planning step generates a structured approach for solving the task. The resulting plan is then executed to produce the final response.

This workflow is intended to encourage decomposition of complex problems into smaller and more manageable components.

### Planner–Executor–Reviewer

The Planner–Executor–Reviewer architecture extends the previous workflow by introducing an additional review stage. After execution, a reviewer component evaluates the generated output and provides feedback intended to identify omissions, inconsistencies, or potential improvements.

The final response is produced after incorporating the review process into the workflow.

All workflow architectures were implemented using Workflow Version V1.4.4 and remained unchanged throughout official data collection.

## 3.4 Foundation Model Providers

The study evaluated three commercially available foundation model providers representing leading contemporary large language model ecosystems.

The evaluated providers were:

* OpenAI GPT-5.5
* Google Gemini 2.5 Pro
* Anthropic Claude Sonnet 4.6

Provider selection was motivated by their widespread adoption, advanced reasoning capabilities, and relevance to current enterprise AI deployments.

To improve comparability, identical task inputs, workflow structures, and prompt templates were applied across providers whenever technically feasible.

## 3.5 Evaluation Framework

System performance was evaluated using both effectiveness and operational metrics.

Effectiveness metrics included:

* Quality score
* Confidence score

Quality score served as the primary performance measure and was used to assess task completion effectiveness across experimental conditions.

Confidence score captured model-reported confidence and was analyzed separately from objective quality measures.

Operational metrics included:

* Cost (USD)
* Execution duration (seconds)
* Total token consumption

These metrics were included to quantify the resource implications associated with increasingly sophisticated workflow architectures.

The use of both effectiveness and efficiency metrics enabled evaluation of performance trade-offs rather than focusing exclusively on output quality.

## 3.6 Data Collection Procedure

Data collection was performed using a standardized execution protocol.

All benchmark tasks were executed under controlled workflow conditions using frozen prompt templates and fixed workflow definitions. Prompt Version frozen_v1.1 and Workflow Version V1.4.4 were maintained throughout the study to prevent procedural drift.

Execution results were recorded in structured datasets that captured task metadata, workflow identifiers, provider information, evaluation outcomes, operational metrics, and execution logs.

Operational anomalies were documented during data collection. Retry events and execution issues were recorded separately to preserve transparency and facilitate later analysis. No final execution failures were included in the analysis dataset.

Upon completion of data collection, provider-specific datasets were merged into a unified analysis-ready dataset. Dataset validation procedures were subsequently performed to verify completeness, consistency, and readiness for statistical analysis.

The resulting dataset formed the basis for all descriptive statistics, assumption testing, analysis of variance procedures, effect size estimation, and publication assets reported in this study.

## 3.7 Reproducibility Strategy

Reproducibility was a primary design consideration throughout the study. To support transparent evaluation and facilitate future replication efforts, all major experimental components were version controlled and frozen during official data collection.

Workflow definitions were maintained under Workflow Version V1.4.4, while prompt templates were preserved under Prompt Version frozen_v1.1. Benchmark tasks were sourced from a fixed task bank (task_bank_v1), ensuring that all providers were evaluated against identical task requirements. These controls were intended to minimize procedural drift and prevent unintentional changes to the experimental configuration during execution.

In addition to preserving workflow and prompt versions, the study maintained structured datasets, execution logs, analysis scripts, statistical outputs, publication tables, and publication figures within a version-controlled research repository. Intermediate processing steps were documented to enable traceability from raw execution outputs to final analytical results.

The analysis pipeline was also preserved through dedicated statistical scripts covering assumption testing, analysis of variance procedures, and effect size estimation. This approach reduces dependence on manual calculations and improves transparency regarding the generation of reported results.

Although exact replication of commercial foundation model behavior cannot be guaranteed due to provider-side system evolution, the study design provides a reproducible record of the evaluated workflows, prompts, tasks, datasets, and analytical procedures.

## 3.8 Workflow Standardization

A central methodological objective of the study was to isolate the effects of provider selection and workflow architecture while minimizing alternative sources of variation.

To achieve this objective, workflow logic was standardized across all providers. Each provider was evaluated using the same workflow structures, identical task definitions, common prompt templates, and equivalent execution procedures. The benchmark task set, evaluation criteria, and data collection process were likewise held constant throughout the study.

This standardization strategy was intended to reduce confounding influences that frequently complicate comparisons across foundation models. In many practical evaluations, differences in prompts, task formulations, implementation details, or execution environments make it difficult to determine whether observed performance differences arise from the models themselves or from surrounding experimental conditions.

By maintaining a consistent workflow implementation and evaluation framework across providers, the study increases confidence that observed differences are primarily associated with the experimental variables under investigation rather than uncontrolled procedural variation.

Consequently, the study should be interpreted as a controlled comparison of workflow-provider combinations operating under a common experimental framework.

## 3.9 Study Positioning

The present study forms the second phase of a broader research program examining the performance of agentic workflow architectures.

Study 001 evaluated Basic Agent, Planner–Executor, and Planner–Executor–Reviewer workflows using a single foundation model provider. That study established that workflow architecture can influence performance across Knowledge, Reasoning, and Coding tasks and demonstrated measurable differences between workflow designs.

Building upon those findings, Study 002 extends the investigation through a controlled cross-provider evaluation. Rather than introducing new workflow architectures, the study preserves the workflow structures established in the earlier work and examines their behavior across multiple foundation model providers. This design enables direct assessment of whether workflow effects observed in a single-provider setting remain observable when the underlying model provider changes.

The resulting methodology combines replication and extension. It replicates the core workflow comparison established in Study 001 while extending the experimental scope to include OpenAI GPT-5.5, Google Gemini 2.5 Pro, and Anthropic Claude Sonnet 4.6. This approach strengthens the evidence base regarding workflow effectiveness and provides insight into how workflow architecture and provider selection interact within contemporary agentic AI systems.

