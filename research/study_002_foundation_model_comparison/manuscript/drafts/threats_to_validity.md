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
