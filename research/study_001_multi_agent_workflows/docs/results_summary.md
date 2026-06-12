# Results Summary

## Overview

The experiment evaluated three agentic workflow architectures across a dataset of 30 enterprise-oriented tasks. Each task was executed using three different workflow configurations, resulting in a total of 90 experimental runs.

The evaluated workflow architectures were:

* Basic Agent
* Planner Executor
* Planner Executor Reviewer

The analysis focused on workflow confidence, task category performance, task difficulty performance, and workflow improvement relative to the Basic Agent baseline.

---

## Workflow Performance

The first objective of the study was to compare overall workflow performance.

The Basic Agent workflow achieved an average confidence score of 0.950. The Planner Executor workflow improved the average confidence score to 0.980, while the Planner Executor Reviewer workflow achieved the highest average confidence score of 0.987.

In addition to achieving the highest confidence score, the Planner Executor Reviewer workflow demonstrated significantly greater consistency across tasks. Both multi-agent workflows produced substantially lower standard deviation values compared with the Basic Agent workflow, indicating more stable behavior across diverse task types.

One notable observation was the presence of a single outlier in the Basic Agent workflow. During the task "Analyze employee feedback and identify major organizational themes," the workflow returned a confidence score of 0.0, which contributed to the higher variance observed in the single-agent architecture.

Overall, the results suggest that introducing planning and review stages improves both confidence and consistency.

---

## Performance by Task Category

Task performance varied across the three task categories.

Coding tasks achieved the highest confidence scores across all workflow architectures. Confidence scores remained near 1.0 regardless of workflow design, suggesting that the underlying model was already highly effective at solving coding-oriented tasks.

Knowledge tasks showed moderate improvements as workflow complexity increased. The Planner Executor Reviewer workflow achieved the highest confidence score within this category, indicating that review and refinement contributed to improved response quality.

The largest differences appeared in Reasoning tasks. The Basic Agent workflow achieved an average confidence score of 0.880, while the Planner Executor and Planner Executor Reviewer workflows achieved 0.968 and 0.979 respectively.

These findings suggest that multi-agent orchestration provides the greatest benefit when solving tasks that require planning, analysis, and multi-step reasoning.

---

## Performance by Task Difficulty

Performance was also analyzed according to task difficulty.

Easy and Medium tasks produced consistently high confidence scores across all workflow architectures. Differences between workflows were relatively small for these tasks.

In contrast, Hard tasks revealed substantial differences between architectures. The Basic Agent workflow achieved an average confidence score of 0.896, while Planner Executor increased confidence to 0.980 and Planner Executor Reviewer further improved confidence to 0.987.

This pattern indicates that workflow architecture becomes increasingly important as task complexity grows.

The results suggest that planning and review mechanisms help reduce uncertainty when addressing difficult or cognitively demanding tasks.

---

## Workflow Improvement

To quantify the benefits of multi-agent architectures, workflow performance was compared against the Basic Agent baseline.

The Planner Executor workflow improved overall confidence by approximately 3.16%, while the Planner Executor Reviewer workflow improved overall confidence by approximately 3.89%.

The largest gains were observed in Reasoning tasks. Relative to the Basic Agent workflow, Planner Executor improved performance by approximately 10.0%, while Planner Executor Reviewer improved performance by approximately 11.25%.

Similarly, Hard tasks showed improvements of approximately 9.38% and 10.16% for Planner Executor and Planner Executor Reviewer respectively.

These results indicate that multi-agent architectures provide their greatest value in scenarios requiring deeper reasoning and greater task complexity.

---

## Key Findings

The experiment produced four primary findings.

First, multi-agent workflows consistently outperformed the single-agent baseline.

Second, the Planner Executor Reviewer workflow achieved the highest overall confidence and the most consistent performance.

Third, Reasoning tasks benefited the most from workflow decomposition and review.

Finally, the performance advantage of multi-agent architectures increased as task difficulty increased.

Taken together, these findings support the hypothesis that agentic workflow architectures can improve the effectiveness and reliability of enterprise-oriented AI systems.
