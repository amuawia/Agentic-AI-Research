# 7. Discussion

The objective of Study 002 was to evaluate the relative impact of foundation model provider and workflow architecture on task performance under controlled experimental conditions. By maintaining identical task sets, prompts, workflow logic, and evaluation criteria across providers, the study isolated the effects of provider selection and workflow design on quality, confidence, and operational performance.

## 7.1 Workflow Architecture Influenced Quality More Than Provider Selection

One of the most notable findings of this study is that workflow architecture exerted a stronger influence on quality score than provider selection. The effect size associated with workflow architecture (partial η² = 0.099) exceeded that of provider selection (partial η² = 0.024), suggesting that the structure through which a model is guided may be more important than the specific foundation model itself for achieving higher-quality outcomes.

This result extends the findings of Study 001, which demonstrated performance differences among Basic Agent, Planner–Executor, and Planner–Executor–Reviewer architectures using a single provider. By replicating the workflow comparison across three major foundation model providers, Study 002 provides additional evidence that workflow design is a critical factor in agentic system performance.

A possible explanation is that planning and task decomposition reduce the cognitive burden associated with solving complex tasks in a single generation step. Structured workflows may encourage more systematic reasoning, improve task coverage, and reduce omissions relative to single-agent approaches. However, the results also indicate that workflow complexity alone does not guarantee improved performance under all conditions.

## 7.2 Workflow Effectiveness Was Provider-Dependent

The significant Provider × Workflow interaction observed for quality score represents one of the most important findings of the study. Although workflow architecture generally influenced quality, the magnitude and direction of workflow effects varied across providers.

This finding suggests that workflow architectures should not be assumed to transfer uniformly between foundation models. A workflow that produces substantial gains with one provider may produce smaller gains, negligible gains, or even performance degradation with another provider. The observed interaction highlights the importance of jointly evaluating workflow architecture and foundation model selection rather than treating them as independent design decisions.

From a practical perspective, organizations adopting agentic systems may benefit from workflow-specific benchmarking rather than assuming that a workflow validated on one model will produce equivalent outcomes on alternative providers. The results therefore support a co-design perspective in which workflow architecture and foundation model capabilities are evaluated together.

## 7.3 Confidence and Quality Represent Distinct Dimensions of Performance

The analyses revealed different patterns for quality and confidence. While workflow architecture demonstrated the strongest effect on quality, provider selection exerted the strongest influence on confidence.

This divergence suggests that confidence and quality should not be treated as interchangeable measures of system performance. Models that express higher confidence do not necessarily achieve the highest objective quality scores, and improvements in workflow architecture may affect answer quality more strongly than self-reported confidence.

The finding has methodological implications for future evaluations of agentic systems. Studies that rely heavily on confidence measures may overlook important differences in objective task performance. Consequently, confidence should be interpreted as a complementary metric rather than a direct proxy for answer quality.

## 7.4 Performance Improvements Incur Operational Costs

A consistent trend across all providers was the increase in operational resource consumption associated with more sophisticated workflow architectures. Cost, execution duration, and token consumption increased systematically as workflows progressed from Basic Agent to Planner–Executor and subsequently to Planner–Executor–Reviewer configurations.

These results illustrate a fundamental trade-off in agentic system design. More complex workflows often provide quality improvements, but such improvements require additional computational resources and longer execution times. The Planner–Executor–Reviewer architecture was particularly resource intensive, consuming substantially more tokens than the Basic Agent configuration while also increasing latency and monetary cost.

For production deployments, these trade-offs may be as important as quality improvements themselves. Organizations operating under budget, latency, or throughput constraints may determine that smaller quality gains do not justify substantially higher operational costs. Consequently, workflow selection should be informed by both effectiveness and efficiency considerations.

## 7.5 Implications for Agentic AI Research

The findings contribute to the growing body of research examining agentic workflows and multi-stage reasoning systems. Rather than focusing exclusively on model scaling or provider selection, the results indicate that workflow design represents an independent source of performance variation that can meaningfully influence outcomes.

The study also demonstrates the value of controlled cross-provider evaluations. Much of the existing literature evaluates workflow architectures using a single foundation model, making it difficult to determine whether reported benefits generalize across providers. By applying identical workflows to multiple leading foundation models, the present study provides evidence that workflow effects are real but provider-dependent.

These findings support future research examining how specific workflow components, such as planning, reflection, verification, or review mechanisms, interact with model characteristics. Understanding these interactions may be critical for developing more effective and resource-efficient agentic systems.

## 7.6 Scope of Interpretation

The conclusions of this study should be interpreted within the boundaries of the experimental design. The findings are based on three foundation model providers, three workflow architectures, and a benchmark consisting of 30 enterprise-oriented tasks executed under Workflow Version V1.4.4 and Prompt Version frozen_v1.1.

Accordingly, the results should not be interpreted as establishing universally optimal workflows or providers. Provider capabilities, pricing structures, model implementations, and API behavior may evolve over time. Furthermore, alternative task domains, workflow designs, or evaluation methodologies may produce different outcomes.

Within the evaluated experimental setting, however, the results provide consistent evidence that workflow architecture is a major determinant of answer quality, that workflow effectiveness varies across providers, and that performance gains are accompanied by measurable operational trade-offs.
