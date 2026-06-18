import os
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

DATASET = r"research/study_002_foundation_model_comparison/datasets/merged/Agentic_AI_Experiments_Main_Study002_V1.4.4_270Runs_AnalysisReady.xlsx"
OUTPUT = r"research/study_002_foundation_model_comparison/analysis/statistical_outputs/anova_results.xlsx"

PROVIDER_COL = "Provider"
WORKFLOW_COL = "workflow_type"
OUTCOMES = ["quality_score", "confidence"]
ALPHA = 0.05


def clean_anova_table(anova_table, outcome):
    table = anova_table.reset_index().rename(columns={"index": "Source"})
    table["Outcome"] = outcome

    table = table.rename(columns={
        "sum_sq": "SS",
        "df": "df",
        "F": "F",
        "PR(>F)": "p_value"
    })

    error_ss = table.loc[table["Source"] == "Residual", "SS"].iloc[0]

    table["Partial_Eta_Squared"] = table.apply(
        lambda row: row["SS"] / (row["SS"] + error_ss)
        if row["Source"] != "Residual" else None,
        axis=1
    )

    table["Significant"] = table["p_value"].apply(
        lambda p: "Yes" if pd.notna(p) and p < ALPHA else "No"
    )

    table["Source"] = table["Source"].replace({
        f"C({PROVIDER_COL})": "Provider",
        f"C({WORKFLOW_COL})": "Workflow",
        f"C({PROVIDER_COL}):C({WORKFLOW_COL})": "Provider × Workflow",
        "Residual": "Error"
    })

    return table[["Outcome", "Source", "SS", "df", "F", "p_value", "Partial_Eta_Squared", "Significant"]]


def run_anova(df, outcome):
    formula = f"{outcome} ~ C({PROVIDER_COL}) * C({WORKFLOW_COL})"
    model = ols(formula, data=df).fit()

    # Type II ANOVA is appropriate for balanced factorial designs.
    anova_table = anova_lm(model, typ=2)

    return clean_anova_table(anova_table, outcome)


def run_tukey(df, outcome, factor_name, group_series):
    tukey = pairwise_tukeyhsd(
        endog=df[outcome],
        groups=group_series,
        alpha=ALPHA
    )

    result = pd.DataFrame(
        data=tukey.summary().data[1:],
        columns=tukey.summary().data[0]
    )

    result.insert(0, "Outcome", outcome)
    result.insert(1, "Comparison_Factor", factor_name)

    return result


def main():
    df = pd.read_excel(DATASET)

    required_cols = [PROVIDER_COL, WORKFLOW_COL] + OUTCOMES
    missing = [col for col in required_cols if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.dropna(subset=required_cols).copy()

    df[PROVIDER_COL] = df[PROVIDER_COL].astype(str)
    df[WORKFLOW_COL] = df[WORKFLOW_COL].astype(str)
    df["Provider_Workflow"] = df[PROVIDER_COL] + " | " + df[WORKFLOW_COL]

    overview = pd.DataFrame({
        "Item": [
            "Dataset",
            "Total Observations",
            "Providers",
            "Workflows",
            "Design",
            "Cell Size",
            "Method",
            "ANOVA Type",
            "Outcomes",
            "Alpha",
            "Status"
        ],
        "Value": [
            "Study 002 AnalysisReady",
            len(df),
            df[PROVIDER_COL].nunique(),
            df[WORKFLOW_COL].nunique(),
            "3 × 3 factorial design",
            "30 observations per provider × workflow group",
            "Two-Way ANOVA",
            "Type II ANOVA",
            ", ".join(OUTCOMES),
            ALPHA,
            "Completed"
        ]
    })

    anova_results = {}
    posthoc_results = []
    interaction_rows = []
    decision_rows = []

    for outcome in OUTCOMES:
        result = run_anova(df, outcome)
        anova_results[outcome] = result

        interaction_row = result[result["Source"] == "Provider × Workflow"].iloc[0]
        interaction_sig = interaction_row["p_value"] < ALPHA

        interaction_rows.append({
            "Outcome": outcome,
            "Interaction_p_value": interaction_row["p_value"],
            "Interaction_Significant": "Yes" if interaction_sig else "No",
            "Interpretation": (
                "Provider effects vary by workflow architecture."
                if interaction_sig
                else "No statistically significant provider × workflow interaction detected."
            )
        })

        for source in ["Provider", "Workflow", "Provider × Workflow"]:
            row = result[result["Source"] == source].iloc[0]
            decision_rows.append({
                "Outcome": outcome,
                "Effect": source,
                "F": row["F"],
                "p_value": row["p_value"],
                "Partial_Eta_Squared": row["Partial_Eta_Squared"],
                "Decision": "Significant" if row["p_value"] < ALPHA else "Not significant"
            })

        provider_p = result.loc[result["Source"] == "Provider", "p_value"].iloc[0]
        workflow_p = result.loc[result["Source"] == "Workflow", "p_value"].iloc[0]
        interaction_p = result.loc[result["Source"] == "Provider × Workflow", "p_value"].iloc[0]

        if provider_p < ALPHA:
            posthoc_results.append(run_tukey(df, outcome, "Provider", df[PROVIDER_COL]))

        if workflow_p < ALPHA:
            posthoc_results.append(run_tukey(df, outcome, "Workflow", df[WORKFLOW_COL]))

        if interaction_p < ALPHA:
            posthoc_results.append(run_tukey(df, outcome, "Provider × Workflow", df["Provider_Workflow"]))

    interaction_df = pd.DataFrame(interaction_rows)
    decision_df = pd.DataFrame(decision_rows)

    if posthoc_results:
        posthoc_df = pd.concat(posthoc_results, ignore_index=True)
    else:
        posthoc_df = pd.DataFrame({
            "Note": ["No post-hoc comparisons were required because no tested effect was significant."]
        })

    quality_anova = anova_results["quality_score"]
    confidence_anova = anova_results["confidence"]

    with pd.ExcelWriter(OUTPUT, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        overview.to_excel(writer, sheet_name="Overview", index=False)
        quality_anova.to_excel(writer, sheet_name="Quality_ANOVA", index=False)
        confidence_anova.to_excel(writer, sheet_name="Confidence_ANOVA", index=False)
        interaction_df.to_excel(writer, sheet_name="Interaction_Analysis", index=False)
        posthoc_df.to_excel(writer, sheet_name="PostHoc", index=False)
        decision_df.to_excel(writer, sheet_name="ANOVA_Decision", index=False)

    print("Two-Way ANOVA completed.")
    print(f"Results saved to: {OUTPUT}")


if __name__ == "__main__":
    main()