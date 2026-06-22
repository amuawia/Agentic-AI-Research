# 6. Results

## 6.1 Dataset and Analysis Overview

The final Study 002 dataset contained 270 successful experimental runs from a balanced 3 × 3 factorial design: three foundation model providers, three workflow architectures, and 30 benchmark tasks. Each provider × workflow cell contained 30 observations. The task bank contained 10 Knowledge, 10 Reasoning, and 10 Coding tasks. Difficulty labels were available as secondary annotations and were not the primary balancing criterion.

All primary analytical variables were available in the analysis-ready dataset, including the operational quality proxy (`quality_score`), confidence, estimated cost, execution duration, total token consumption, and model call count. The generated publication package includes `publication_tables_v2.md`, `publication_tables_v2.xlsx`, and four current publication figures in `results/figures_publication/`. Table 1 reports provider × workflow descriptive summaries; Table 2 reports task-category summaries; Table 3 reports secondary difficulty annotations; and Table 4 reports operational-efficiency rankings.

## 6.2 RQ1: Workflow Effects on the Operational Quality Proxy

Workflow architecture was significantly associated with the operational quality proxy, F = 14.329, p < 0.001, partial η² = 0.099. This was the largest main effect observed for quality and is interpreted as a medium effect. Provider selection also had a statistically significant but smaller effect, F = 3.186, p = 0.043, partial η² = 0.024.

Across workflows, Planner–Executor achieved the highest mean quality proxy (M = 0.944), followed by Basic Agent (M = 0.905) and Planner–Executor–Reviewer (M = 0.822). Table 1 and Figure 1 (`figure_01_quality_heatmap_provider_workflow.png`) summarize mean quality by provider × workflow condition. These results indicate that adding a planning stage was associated with stronger operational quality-proxy outcomes in this benchmark, but adding a reviewer stage did not uniformly improve the proxy metric.

## 6.3 RQ2: Provider Effects on Confidence and Operational Outcomes

Provider selection was more strongly associated with confidence than with the operational quality proxy. For confidence, provider had a significant medium effect, F = 12.209, p < 0.001, partial η² = 0.086. Workflow architecture also had a statistically significant but smaller effect on confidence, F = 3.624, p = 0.028, partial η² = 0.027.

Mean confidence differed across providers, with Google showing the highest mean confidence (M = 0.964), followed by OpenAI (M = 0.942) and Anthropic (M = 0.886). Because confidence is model-reported, these findings should be interpreted as differences in provider self-assessment behavior rather than externally verified correctness.

## 6.4 RQ3: Provider × Workflow Interaction

The provider × workflow interaction was significant for the operational quality proxy, F = 4.673, p = 0.001, partial η² = 0.067. This medium interaction effect indicates that workflow behavior differed across providers. For example, Google achieved a high mean quality proxy under Planner–Executor but a lower mean under Planner–Executor–Reviewer, while OpenAI showed more stable quality-proxy behavior across workflow conditions.

For confidence, the provider × workflow interaction was not statistically significant, F = 2.022, p = 0.092, partial η² = 0.030. This contrast suggests that workflow-provider interactions were more visible in the operational quality proxy than in confidence.

## 6.5 Measurement-Validity Audit

The measurement-validity audit showed that `quality_score` and confidence were identical for all Basic Agent observations and all Planner–Executor observations. In contrast, they were mostly distinct in the Planner–Executor–Reviewer workflow: only 5 of 90 reviewer-workflow observations (5.6%) had identical quality and confidence values.

This finding is central to interpretation. For non-reviewer workflows, the operational quality proxy overlaps with confidence when no independent quality score is emitted. For the reviewer workflow, the review stage can produce a distinct score. Therefore, quality-related results in this study should be read as operational workflow-generated proxy evidence, not as independent human-rated answer quality.

## 6.6 Robustness, Task-Stratified, and Efficiency Findings

Robustness outputs supported cautious interpretation of the main descriptive pattern. Median quality was 0.950 for Basic Agent, 0.950 for Planner–Executor, and 0.880 for Planner–Executor–Reviewer. Bootstrap and outlier-sensitivity outputs were generated to document stability without treating them as replacements for independent validation.

Task-stratified analysis showed category-level variation. Mean quality proxy was highest for Knowledge tasks (M = 0.919), followed by Reasoning tasks (M = 0.900) and Coding tasks (M = 0.853). Table 2 and Figure 2 (`figure_02_quality_by_task_category.png`) summarize these category-level results. Table 3 reports difficulty-annotation summaries; these are exploratory because difficulty was a secondary annotation layer rather than a balancing criterion.

Operational-efficiency analysis showed that workflow complexity increased resource requirements. Basic Agent had the lowest mean cost and duration, while Planner–Executor–Reviewer had the highest resource use. Figure 3 (`figure_03_cost_quality_tradeoff.png`) presents the cost–quality trade-off, while Table 4 and Figure 4 (`figure_04_operational_efficiency_ranking.png`) summarize the top configurations by a descriptive balanced-efficiency index. These results indicate that workflow selection involves practical trade-offs among quality proxy, cost, latency, and token usage.
