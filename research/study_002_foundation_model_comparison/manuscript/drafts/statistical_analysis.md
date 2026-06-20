# 5. Statistical Analysis

## 5.1 Analysis Objectives

The statistical analysis was designed to evaluate the relative effects of foundation model provider and workflow architecture on agentic AI system performance. In addition to examining the independent contributions of these factors, the analysis sought to determine whether workflow effectiveness varied across providers.

The primary analytical objectives were:

* To quantify performance differences between foundation model providers.
* To quantify performance differences between workflow architectures.
* To evaluate interaction effects between provider selection and workflow architecture.
* To assess the magnitude of observed effects using effect size measures.
* To characterize operational trade-offs associated with workflow complexity.

The primary outcome variables analyzed in this study were quality score and confidence. Additional operational metrics, including cost, execution duration, and total token consumption, were examined using descriptive statistical methods.

## 5.2 Dataset Preparation

Statistical analyses were conducted using the frozen analysis dataset generated following completion of data collection and validation procedures.

Prior to formal analysis, the dataset was examined for completeness and consistency. Validation procedures confirmed that no missing values were present in the primary outcome variables, including quality score, confidence, cost, duration, and token consumption. Provider allocations and workflow allocations were verified to be consistent with the experimental design.

The final analysis dataset contained 270 observations distributed across three providers and three workflow architectures. This dataset served as the sole source for all descriptive statistics, assumption testing, inferential analyses, and effect size calculations reported in the study.

## 5.3 Assumption Testing

Before conducting inferential statistical analyses, assumption testing procedures were performed to evaluate the suitability of the dataset for analysis of variance methods.

The assessment focused on the assumptions commonly associated with factorial ANOVA, including distributional characteristics and variance behavior across experimental groups. Formal assumption testing outputs were generated and reviewed prior to hypothesis testing.

The purpose of these procedures was not to establish perfect conformity to theoretical assumptions but rather to identify substantial violations that could undermine the validity of subsequent analyses. Given the balanced structure of the experimental design and the sample sizes available within the study, ANOVA was considered an appropriate analytical approach for evaluating the primary research questions.

All assumption testing results were documented and preserved within the study's statistical output files to ensure transparency and reproducibility.

## 5.4 Analysis of Variance

The primary inferential analyses were conducted using two-way analysis of variance (ANOVA).

Two-way ANOVA was selected because the experimental design included two categorical independent variables, foundation model provider and workflow architecture, and because the study sought to evaluate both main effects and interaction effects.

Separate ANOVA models were performed for quality score and confidence.

The analysis framework enabled evaluation of:

* The main effect of provider.
* The main effect of workflow architecture.
* The Provider × Workflow interaction effect.

The inclusion of interaction effects was particularly important because workflow architectures may not exhibit identical behavior across different foundation model providers. Examining interaction effects therefore provided additional insight beyond simple comparisons of average performance.

This analytical approach aligned directly with the factorial structure of the experimental design and allowed simultaneous assessment of multiple sources of variation within a unified statistical framework.

## 5.5 Effect Size Estimation

Statistical significance alone does not indicate the practical importance of an observed effect. Consequently, effect size estimation was performed in addition to significance testing.

Partial eta squared (partial η²) was used as the primary measure of effect magnitude for ANOVA results. Effect size estimates were calculated for provider effects, workflow effects, and interaction effects.

The inclusion of effect size measures enabled evaluation of the relative influence of experimental factors and supported interpretation beyond binary significance decisions. This was particularly important because large sample sizes may produce statistically significant findings even when practical effects are limited.

Effect size results were reported alongside ANOVA findings throughout the study and were incorporated into the interpretation of performance differences between providers and workflow architectures.

## 5.6 Significance Thresholds and Reporting

Statistical significance was evaluated using a threshold of α = 0.05.

For each inferential analysis, test statistics, p-values, and effect size estimates were reported to support transparent interpretation of results. Findings were interpreted using both statistical significance and effect magnitude rather than relying exclusively on p-values.

Descriptive statistics were reported to summarize central tendencies and variability across providers and workflow architectures. Inferential results were subsequently used to evaluate the study hypotheses and identify meaningful performance differences within the experimental design.

All statistical outputs, including descriptive statistics, assumption tests, ANOVA results, and effect size calculations, were preserved within the study repository as part of the reproducibility package.

## 5.7 Rationale for Analytical Approach

The analytical approach was selected to align with the factorial structure of the experimental design. Because the study simultaneously examined multiple foundation model providers and multiple workflow architectures, an analytical method capable of evaluating both independent and combined effects was required.

Two-way ANOVA provides a suitable framework for such investigations because it enables simultaneous assessment of main effects and interaction effects within a single model. This capability was particularly important for the present study because a central research question concerned whether workflow effectiveness remained consistent across providers.

Alternative approaches based solely on pairwise comparisons would have provided less information regarding interaction behavior and would not have aligned as closely with the structure of the experimental design. Consequently, the selected analytical framework supported a more comprehensive evaluation of the relationships among the experimental variables.

## 5.8 Statistical Reproducibility

To support transparency and reproducibility, all statistical procedures were preserved through dedicated analysis scripts and documented output files.

The analytical workflow included dataset validation, descriptive statistics generation, assumption testing, analysis of variance procedures, and effect size estimation. Intermediate outputs and final statistical results were retained within the study repository to provide traceability between the analysis-ready dataset and reported findings.

The preservation of scripts, datasets, and statistical outputs reduces dependence on manual calculations and facilitates future verification of reported results. This approach also supports independent replication efforts and aligns with emerging expectations regarding reproducible empirical AI research.
