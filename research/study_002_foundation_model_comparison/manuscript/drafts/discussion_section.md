# 7. Discussion

The objective of Study 002 was to evaluate the relative influence of foundation model provider and workflow architecture on performance under controlled experimental conditions. By maintaining identical tasks, prompts, workflow logic, and evaluation procedures across providers, the study isolated the effects of provider selection and workflow design on answer quality, confidence, and operational efficiency.

The results demonstrate that both provider selection and workflow architecture contribute to performance variation. However, their influence differs depending on the outcome measure being considered. Workflow architecture exhibited a stronger association with quality outcomes, whereas provider selection exerted a stronger influence on confidence. Furthermore, workflow effectiveness was not uniform across providers, highlighting the importance of considering workflow design and foundation model selection jointly rather than as independent factors.

## 7.1 Workflow Architecture Influenced Quality More Than Provider Selection

One of the most important findings of the study is that workflow architecture had a larger effect on quality score than provider selection. The observed effect size for workflow architecture exceeded that of provider selection, suggesting that the manner in which a model is guided through a task can be more influential than the underlying model provider itself.

This finding aligns with the broader motivation behind agentic AI systems. Rather than relying exclusively on improvements in foundation model capability, agentic workflows seek to improve outcomes through structured reasoning, planning, decomposition, verification, and review. The results of the present study suggest that such workflow-level interventions can produce measurable quality improvements even when the underlying foundation model remains unchanged.

A plausible explanation is that workflow architectures reduce the complexity of solving a task within a single generation step. Planning stages may encourage more systematic task decomposition, while execution and review stages may reduce omissions and improve consistency. Consequently, workflow architecture can be viewed as an additional optimization layer that operates independently of the foundation model itself.

The findings therefore suggest that organizations seeking quality improvements should consider workflow engineering as a primary design variable rather than focusing exclusively on model selection.

## 7.2 Workflow Effectiveness Was Provider-Dependent

Although workflow architecture generally influenced quality, the significant Provider × Workflow interaction demonstrates that workflow effectiveness varied across providers.

This result is particularly important because many workflow studies evaluate a single foundation model and implicitly assume that observed workflow benefits will generalize to alternative providers. The present findings suggest that such assumptions may not always hold. Identical workflow architectures produced different performance patterns when paired with different foundation models.

Several explanations may account for this behavior. Foundation models differ in training data, instruction-following characteristics, reasoning capabilities, context utilization strategies, and response generation mechanisms. These differences may influence how effectively a model responds to planning, decomposition, or review stages embedded within a workflow.

From a practical perspective, the results indicate that workflow selection should not be separated from model selection. Organizations evaluating agentic systems may benefit from benchmarking complete workflow-provider combinations rather than independently optimizing workflows and models. A workflow that performs well with one provider cannot automatically be assumed to provide equivalent benefits when deployed with another.

The observed interaction effect therefore supports a co-design perspective in which workflow architecture and foundation model capabilities are treated as interdependent components of an agentic system.

## 7.3 Confidence and Quality Represent Distinct Dimensions of Performance

The analyses revealed an important distinction between confidence and quality outcomes. While workflow architecture exhibited the strongest influence on quality score, provider selection demonstrated the strongest influence on confidence.

This divergence suggests that confidence should not be interpreted as a direct substitute for objective performance. Models may express high confidence despite producing lower-quality outputs, while workflow modifications may improve answer quality without producing equivalent changes in confidence.

The finding has methodological implications for future evaluations of agentic systems. Studies that rely heavily on confidence measures may overlook meaningful differences in actual task performance. Confidence can provide useful information regarding model behavior and self-assessment, but it should be interpreted alongside objective evaluation metrics rather than as a standalone indicator of effectiveness.

More broadly, the results reinforce the importance of multi-dimensional evaluation frameworks. Agentic systems should be assessed using multiple performance indicators because no single metric fully captures system effectiveness.

## 7.4 Performance Improvements Incur Operational Costs

The study also demonstrated a consistent relationship between workflow complexity and operational resource consumption. Across all providers, increases in workflow sophistication were associated with higher monetary cost, longer execution duration, and greater token consumption.

This finding highlights a fundamental trade-off in agentic system design. More sophisticated workflows frequently improve performance, but such improvements are not obtained without additional computational expense. The Planner–Executor–Reviewer architecture produced the highest resource requirements across multiple operational metrics, reflecting the cost of incorporating planning and review stages into the execution process.

For enterprise deployments, these trade-offs may be as important as quality improvements themselves. Organizations often operate under budgetary, latency, throughput, or infrastructure constraints. In such environments, the most effective workflow may not necessarily be the workflow that achieves the highest quality score. Instead, decision makers may need to balance quality improvements against increases in cost and execution time.

The findings therefore support the use of efficiency-aware evaluation frameworks that consider both performance and operational requirements when comparing agentic architectures.

## 7.5 Comparison with Study 001

Study 002 extends the findings of Study 001, which evaluated the same workflow architectures using a single foundation model provider. The earlier study demonstrated that workflow design influences performance and that multi-stage workflows can outperform simpler agent configurations under certain conditions.

The present study expands this investigation by introducing multiple foundation model providers while preserving workflow structure, task selection, prompt design, and evaluation methodology. This controlled extension enables direct examination of whether workflow effects persist across providers.

The results indicate that workflow architecture remains an important determinant of performance across providers. However, the significant interaction effect observed in Study 002 reveals an additional layer of complexity that was not observable within a single-provider design. Specifically, workflow effectiveness depends partly on the characteristics of the underlying foundation model.

Consequently, Study 002 not only replicates the general importance of workflow architecture observed in Study 001 but also demonstrates that workflow benefits are conditional rather than universally transferable.

## 7.6 Implications for Enterprise AI Deployment

The findings have several practical implications for organizations adopting agentic AI systems.

First, workflow architecture should be considered a strategic design decision rather than merely an implementation detail. The results indicate that workflow modifications can influence quality outcomes to a degree that exceeds the influence of provider selection alone.

Second, provider evaluation should be conducted within the context of the intended workflow architecture. Benchmarking foundation models in isolation may not accurately reflect production performance when models are embedded within multi-stage workflows.

Third, operational considerations should be incorporated into deployment decisions. In some applications, modest quality improvements may justify substantial increases in computational cost. In others, latency and cost constraints may favor simpler architectures despite lower performance.

Finally, the findings suggest that organizations may benefit from systematic experimentation before large-scale deployment. Because workflow effectiveness varies across providers, empirical validation remains essential for identifying appropriate workflow-provider combinations.

## 7.7 Future Research Directions

Several opportunities for future research emerge from the present study.

First, future investigations could evaluate additional workflow architectures beyond the three examined here. Reflection-based workflows, tool-augmented agents, retrieval-enhanced systems, and collaborative multi-agent configurations may exhibit different performance characteristics and operational trade-offs.

Second, future studies could examine a broader range of foundation model providers and model variants. As commercial and open-source models continue to evolve, understanding how workflow effects interact with model capabilities will remain an important research question.

Third, additional work is needed to explore domain-specific performance. Although the present benchmark included Knowledge, Reasoning, and Coding tasks, alternative domains such as healthcare, finance, scientific research, or legal analysis may exhibit different workflow requirements.

Finally, future research could investigate optimization strategies that improve quality while minimizing resource consumption. Such approaches may be particularly valuable for enterprise environments in which operational efficiency is a critical consideration.

## 7.8 Scope of Interpretation

The conclusions of this study should be interpreted within the boundaries of the experimental design. The findings are derived from three foundation model providers, three workflow architectures, and a benchmark consisting of 30 enterprise-oriented tasks executed using Workflow Version V1.4.4 and Prompt Version frozen_v1.1.

Accordingly, the results should not be interpreted as identifying universally optimal providers or workflows. Provider capabilities, pricing models, inference systems, and API behavior may change over time. Alternative task sets, workflow designs, evaluation criteria, or deployment contexts may also produce different outcomes.

Within the evaluated experimental setting, however, the evidence consistently indicates that workflow architecture is a major determinant of answer quality, that workflow effectiveness varies across providers, and that performance gains are accompanied by measurable operational trade-offs.
