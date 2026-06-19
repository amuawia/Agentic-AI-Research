# 6. Results

## 6.1 Dataset Validation

The final Study 002 dataset contained 270 experimental runs generated from a fully crossed design involving three foundation model providers, three workflow architectures, and 30 benchmark tasks. Each provider contributed 90 observations, and each workflow architecture was evaluated across 90 observations, resulting in a balanced design for the primary experimental factors.

No missing values were identified in the primary outcome variables, including quality score, confidence, cost (USD), execution duration (seconds), and total token consumption. Task metadata were complete for all observations.

The benchmark consisted of Knowledge, Reasoning, and Coding tasks. Although provider and workflow allocations were balanced, task difficulty distribution reflected the composition of the frozen task bank and was therefore not uniform. The final dataset included 63 Easy, 99 Medium, and 108 Hard task executions.

Operational reliability was high throughout data collection. Google Gemini required four documented retry events but produced no final execution failures. Anthropic Claude required one retry event and generated one documented JSON compliance failure. OpenAI GPT-5.5 completed all official runs without recorded retry events or execution failures. All successful executions were retained in the final analysis dataset.

## 6.2 Quality Score Analysis

A two-way analysis of variance (ANOVA) was conducted to evaluate the effects of foundation model provider and workflow architecture on quality score.

The analysis revealed a statistically significant main effect of provider, F = 3.186, p = 0.043, with a small effect size (partial η² = 0.024). A significant main effect of workflow architecture was also observed, F = 14.329, p < 0.001, with a medium effect size (partial η² = 0.099).

Most notably, the Provider × Workflow interaction was statistically significant, F = 4.673, p = 0.001, partial η² = 0.067. This interaction indicates that the relative effectiveness of workflow architectures differed across providers rather than producing uniform performance gains.

Figure 1 presents mean quality scores by provider and workflow architecture. Although more complex workflows generally achieved higher quality scores, the magnitude and direction of improvement varied across providers. For example, Google Gemini demonstrated strong performance under the Planner–Executor configuration but exhibited reduced performance under the Planner–Executor–Reviewer workflow relative to expectations based solely on workflow complexity.

Taken together, these findings suggest that workflow architecture exerted a stronger influence on quality outcomes than provider selection alone. However, the significant interaction effect demonstrates that workflow performance cannot be evaluated independently of the underlying foundation model.

## 6.3 Confidence Analysis

A second two-way ANOVA was performed to examine confidence scores across providers and workflow architectures.

Provider selection had a statistically significant effect on confidence, F = 12.209, p < 0.001, with a medium effect size (partial η² = 0.086). Workflow architecture also demonstrated a statistically significant effect, F = 3.624, p = 0.028, although the corresponding effect size was comparatively small (partial η² = 0.027).

In contrast to the quality score analysis, the Provider × Workflow interaction was not statistically significant, F = 2.022, p = 0.092, partial η² = 0.030.

Figure 2 illustrates confidence scores across experimental conditions. Confidence levels remained relatively high throughout the study, but systematic differences between providers were evident. The absence of a significant interaction effect suggests that confidence was influenced more consistently by provider characteristics than by provider-specific responses to workflow architecture.

Overall, confidence outcomes appeared to be driven primarily by provider selection, whereas workflow architecture played a comparatively smaller role.

## 6.4 Effect Size Summary

Effect size estimates provide additional insight into the relative importance of the experimental factors.

For quality score, workflow architecture produced the largest observed main effect (partial η² = 0.099), exceeding the effect associated with provider selection (partial η² = 0.024). The Provider × Workflow interaction also demonstrated a meaningful effect size (partial η² = 0.067), indicating that workflow effectiveness varied substantially across providers.

For confidence, provider selection produced the strongest effect (partial η² = 0.086), while workflow architecture contributed a smaller effect (partial η² = 0.027). The interaction effect remained comparatively small and did not achieve statistical significance.

These findings suggest that answer quality and model confidence were influenced by different underlying factors. Workflow architecture was more strongly associated with quality outcomes, whereas provider choice was more strongly associated with confidence outcomes.

Complete effect size estimates are reported in Table 4.

## 6.5 Operational Performance Metrics

Operational performance was evaluated using monetary cost, execution duration, and total token consumption.

Across all providers, increasing workflow complexity was consistently associated with increased resource requirements. As illustrated in Figure 3, mean execution cost increased progressively from Basic Agent to Planner–Executor and from Planner–Executor to Planner–Executor–Reviewer configurations.

A similar pattern was observed for execution duration (Figure 4). More complex workflows required substantially longer processing times because additional planning, execution, and review stages increased the total number of model interactions. Google Gemini generally exhibited the longest execution durations under the most complex workflow conditions.

Token consumption followed the same trend (Figure 5). Planner–Executor–Reviewer workflows consumed substantially more tokens than Basic Agent workflows, frequently exceeding five times the average token usage observed in the baseline configuration.

These results demonstrate a clear trade-off between performance and operational efficiency. While more sophisticated workflow architectures often produced improvements in quality, such gains were accompanied by higher costs, longer execution times, and greater token consumption.
