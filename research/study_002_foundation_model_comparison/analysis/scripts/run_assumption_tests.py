import pandas as pd
from scipy.stats import shapiro, levene

DATASET = r"research/study_002_foundation_model_comparison/datasets/merged/Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx"

df = pd.read_excel(DATASET)

provider_col = "Provider"
workflow_col = "workflow_type"

outcomes = ["quality_score", "confidence"]

normality_results = []
levene_results = []

# Shapiro-Wilk by Provider × Workflow group
for outcome in outcomes:
    for (provider, workflow), group in df.groupby([provider_col, workflow_col]):
        values = group[outcome].dropna()

        stat, p_value = shapiro(values)

        normality_results.append({
            "Outcome": outcome,
            "Provider": provider,
            "Workflow": workflow,
            "N": len(values),
            "Shapiro_W": stat,
            "p_value": p_value,
            "Normality_Result": "Normality not rejected" if p_value >= 0.05 else "Normality rejected"
        })

# Levene's Test across Provider × Workflow groups
for outcome in outcomes:
    groups = [
        group[outcome].dropna().values
        for _, group in df.groupby([provider_col, workflow_col])
    ]

    stat, p_value = levene(*groups, center="median")

    levene_results.append({
        "Outcome": outcome,
        "Levene_Statistic": stat,
        "p_value": p_value,
        "Homogeneity_Result": "Equal variances not rejected" if p_value >= 0.05 else "Equal variances rejected"
    })

normality_df = pd.DataFrame(normality_results)
levene_df = pd.DataFrame(levene_results)

OUTPUT = r"research/study_002_foundation_model_comparison/analysis/statistical_outputs/formal_assumption_tests.xlsx"

with pd.ExcelWriter(OUTPUT, engine="openpyxl") as writer:
    normality_df.to_excel(writer, sheet_name="Shapiro_Wilk", index=False)
    levene_df.to_excel(writer, sheet_name="Levene_Test", index=False)

print("Formal assumption tests completed.")
print(f"Output saved to: {OUTPUT}")