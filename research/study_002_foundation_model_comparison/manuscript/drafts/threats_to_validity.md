# 8. Threats to Validity

As with any empirical evaluation of AI systems, the findings of this study should be interpreted in light of several validity considerations. The experimental design incorporated multiple controls intended to improve reproducibility and reduce bias, including frozen prompts, fixed workflow definitions, a standardized task bank, and identical evaluation procedures across providers. Nevertheless, certain limitations remain and should be considered when interpreting the results.

## 8.1 Internal Validity

Internal validity concerns whether the observed outcomes can reasonably be attributed to the experimental factors under investigation rather than to uncontrolled influences.

Several measures were implemented to strengthen internal validity. All providers were evaluated using the same benchmark tasks, workflow architectures, prompt templates, execution procedures, and evaluation criteria. Workflow Version V1.4.4 and Prompt Version frozen_v1.1 were maintained throughout official data collection to minimize procedural variation.

Despite these controls, some factors remained outside direct experimental control. Foundation model providers operate proprietary inference systems whose internal configurations are not publicly accessible. Variations in model serving infrastructure, load balancing, system updates, or inference optimization mechanisms may influence outputs independently of the experimental design.

A small number of operational anomalies were documented during data collection. Google Gemini required four retry events, while Anthropic Claude required one retry event and produced one documented JSON compliance failure. Although these events were recorded and managed according to the study protocol, they illustrate the practical reality that large-scale evaluations of commercial foundation models may be affected by transient API behavior. No final execution failures were retained in the analysis dataset.

In addition, large language models are inherently stochastic systems. Even under identical prompts and workflow configurations, repeated executions may produce different outputs. While the study design sought to evaluate realistic system behavior rather than eliminate stochasticity entirely, execution variability remains a potential source of unexplained variance.

## 8.2 Construct Validity

Construct validity concerns whether the selected metrics accurately represent the concepts that the study intends to measure.

The primary outcome variables included quality score, confidence, cost, execution duration, and total token consumption. While these measures provide useful perspectives on system performance, they do not capture every aspect of agent effectiveness.

Quality scores represent an operationalized measure of task performance rather than a complete assessment of real-world utility. Alternative evaluation frameworks may emphasize different dimensions, including factual accuracy, robustness, interpretability, maintainability, or user satisfaction. Consequently, the quality metric used in this study should be interpreted as one representation of performance rather than a universal measure of agent effectiveness.

Confidence presents an additional construct validity consideration. Confidence scores reflect model-generated self-assessments rather than externally verified measures of certainty. Prior research has shown that confidence and correctness are not always aligned in large language models. Accordingly, confidence was analyzed as a complementary indicator rather than as a direct substitute for objective task quality.

Similarly, operational metrics such as cost, duration, and token consumption provide important information regarding efficiency but do not capture all deployment considerations. Infrastructure costs, rate limits, availability constraints, and integration complexity may also influence the practical suitability of a workflow architecture.

## 8.3 External Validity

External validity concerns the extent to which the findings can be generalized beyond the specific experimental setting.

The study evaluated three major foundation model providers, three workflow architectures, and a benchmark consisting of 30 enterprise-oriented tasks. Although these selections provide meaningful coverage of contemporary agentic AI systems, they do not represent the full range of available models, workflows, or application domains.

The findings therefore should not be interpreted as identifying universally optimal providers or workflow architectures. Alternative foundation models, including future commercial releases or open-source systems, may exhibit different performance characteristics. Likewise, workflow architectures that incorporate retrieval augmentation, tool use, reflection mechanisms, memory systems, or collaborative multi-agent coordination may produce different outcomes than the architectures evaluated in this study.

The benchmark itself represents another limitation. While the task bank includes Knowledge, Reasoning, and Coding tasks, it does not encompass all possible enterprise use cases. Domains such as healthcare, finance, legal analysis, scientific discovery, cybersecurity, and multimodal applications may place different demands on agentic systems.

Task difficulty distribution was intentionally inherited from the frozen benchmark and was therefore not perfectly balanced. The final dataset contained 63 Easy, 99 Medium, and 108 Hard task executions. Although this imbalance reflects the composition of the benchmark rather than unequal provider allocation, alternative task distributions may influence aggregate performance estimates.

Accordingly, the conclusions of this study should be interpreted as applying to the evaluated providers, workflows, task bank, and experimental configuration rather than to all possible agentic AI systems.

## 8.4 Reproducibility and Temporal Validity

A distinctive challenge in foundation model research is the rapidly evolving nature of the underlying systems. Unlike many traditional software platforms, commercial foundation models may change over time through provider-side updates that are not fully transparent to researchers.

To support reproducibility, the study preserved workflow definitions, prompt templates, task bank versions, dataset files, analysis scripts, statistical outputs, publication tables, and publication figures within a version-controlled repository. Workflow Version V1.4.4, Prompt Version frozen_v1.1, and task_bank_v1 were frozen for official data collection and analysis.

Nevertheless, exact replication may become increasingly difficult as providers introduce new model versions, modify inference systems, update pricing structures, or alter API behavior. Consequently, future replications conducted under nominally identical procedures may not produce identical results.

This limitation is not unique to the present study but reflects a broader challenge facing empirical research involving rapidly evolving foundation models. For this reason, the findings should be interpreted as a reproducible evaluation of the evaluated systems at the time of experimentation rather than as immutable estimates of future model performance.

## 8.5 Summary

Despite these limitations, the study incorporates several methodological strengths, including a controlled cross-provider design, frozen workflow and prompt configurations, balanced provider and workflow allocations, comprehensive operational metrics, documented execution logs, and transparent statistical analysis procedures. These measures strengthen confidence in the reported findings while also clarifying the boundaries within which the conclusions should be interpreted.
