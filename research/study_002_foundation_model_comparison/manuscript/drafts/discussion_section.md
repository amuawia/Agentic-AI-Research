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

## 7.5 Implications for Research and Deployment

For researchers, the study shows the value of reporting provider × workflow interactions, measurement-validity audits, and operational metrics alongside primary performance results. For practitioners, it suggests that deployment decisions should not be based on provider reputation or workflow complexity alone. Instead, teams should evaluate the specific configuration they intend to use, using metrics that reflect both output behavior and operational feasibility.

The study also highlights the need for stronger follow-up evaluation. Future work should add independent human ratings, inter-rater reliability, task-specific rubrics, additional providers, open-source models, and additional workflow architectures such as retrieval-augmented, tool-using, reflection-based, and multi-agent designs. Such work would extend the present operational benchmark into a more comprehensive evaluation of agentic AI system quality.
