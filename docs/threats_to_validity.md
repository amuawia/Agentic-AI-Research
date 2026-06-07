# Threats to Validity

## Overview

As with any experimental study, several factors may influence the interpretation and generalizability of the results. This section discusses the primary limitations of the experiment and identifies potential threats to validity.

---

## Model Dependency

All workflow architectures were evaluated using the same underlying language model.

The experiment was conducted using Google Gemini as the execution model for all workflows. While this approach ensured fairness across workflow comparisons, the results may not fully generalize to other large language models such as GPT-4, Claude, or future generations of AI systems.

Different models may respond differently to planning, execution, and review stages, which could influence the magnitude of the observed improvements.

---

## Dataset Size

The study used a dataset consisting of 30 enterprise-oriented tasks.

Although the dataset was intentionally designed to cover multiple categories and difficulty levels, it remains relatively small compared with large-scale benchmark datasets commonly used in AI evaluation.

A larger dataset could provide additional evidence regarding the consistency and robustness of the findings.

---

## Task Selection Bias

The task dataset was manually created and categorized by the researcher.

While effort was made to include realistic enterprise scenarios covering knowledge, reasoning, and coding tasks, the selection process may introduce bias regarding task type, complexity, and expected outcomes.

Different task sets may produce different performance patterns.

---

## Confidence as an Evaluation Metric

The primary metric used in this study was workflow confidence.

Although confidence provides a useful indicator of workflow behavior, it does not directly measure factual correctness or objective task success.

A highly confident response may still contain errors, while a lower-confidence response may be correct.

Future studies could incorporate additional evaluation methods such as expert review, automated benchmarks, or task-specific success criteria.

---

## Reviewer-Generated Quality Scores

Quality scores were only available for the Planner Executor Reviewer workflow.

As a result, quality scores could not be directly compared across all three workflow architectures.

The reviewer-generated scores were used primarily to evaluate the behavior of the Planner Executor Reviewer workflow rather than as a universal comparison metric.

Future work may include external evaluators or independent scoring mechanisms to enable broader comparisons.

---

## Workflow Implementation

The workflows were implemented using n8n and a specific orchestration design.

Alternative implementations of planner, executor, or reviewer architectures may produce different results.

Therefore, the findings should be interpreted as evidence regarding the evaluated workflow implementations rather than definitive conclusions about all possible agentic architectures.

---

## Enterprise Generalization

The experiment focused on enterprise-oriented tasks.

Although many of the evaluated scenarios reflect realistic business use cases, the results may not generalize to other domains such as healthcare, education, scientific research, or highly specialized industrial applications.

Additional studies are required to validate the findings across different environments and task domains.

---

## Internal Validity

Several measures were taken to improve internal validity.

All workflow architectures:

* Used the same language model
* Received the same task prompts
* Operated within the same execution environment
* Followed the same data collection process

These controls help reduce experimental bias and support the fairness of the workflow comparison.

---

## Summary

Despite these limitations, the study provides useful evidence regarding the impact of workflow architecture on AI system performance. The controlled comparison of three agentic workflow designs demonstrates that planning and review mechanisms can improve confidence, consistency, and performance, particularly for reasoning-intensive and difficult tasks.

Future studies using larger datasets, additional language models, and independent evaluation methods would help strengthen and extend these findings.
