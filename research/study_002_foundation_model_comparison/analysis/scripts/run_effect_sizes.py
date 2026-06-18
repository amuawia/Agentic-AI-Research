import pandas as pd

ANOVA_FILE = r"research/study_002_foundation_model_comparison/analysis/statistical_outputs/anova_results.xlsx"
OUTPUT_FILE = r"research/study_002_foundation_model_comparison/analysis/statistical_outputs/effect_sizes.xlsx"


def interpret_partial_eta_squared(value):
    if pd.isna(value):
        return ""
    if value < 0.01:
        return "Negligible"
    if value < 0.06:
        return "Small"
    if value < 0.14:
        return "Medium"
    return "Large"


def load_effect_sizes(sheet_name):
    df = pd.read_excel(ANOVA_FILE, sheet_name=sheet_name)

    df = df[df["Source"] != "Error"].copy()

    df["Effect Size Metric"] = "Partial Eta Squared"
    df["Interpretation"] = df["Partial_Eta_Squared"].apply(
        interpret_partial_eta_squared
    )

    return df[
        [
            "Outcome",
            "Source",
            "Partial_Eta_Squared",
            "Effect Size Metric",
            "Interpretation",
            "Significant",
        ]
    ]


def main():
    quality = load_effect_sizes("Quality_ANOVA")
    confidence = load_effect_sizes("Confidence_ANOVA")

    overview = pd.DataFrame(
        {
            "Item": [
                "Source File",
                "Effect Size Metric",
                "Primary Outcome",
                "Secondary Outcome",
                "Interpretation Thresholds",
                "Status",
            ],
            "Value": [
                "anova_results.xlsx",
                "Partial Eta Squared",
                "quality_score",
                "confidence",
                "0.01 = Small, 0.06 = Medium, 0.14 = Large",
                "Completed",
            ],
        }
    )

    combined = pd.concat([quality, confidence], ignore_index=True)

    interpretation = pd.DataFrame(
        {
            "Threshold": [
                "< 0.01",
                "0.01 to < 0.06",
                "0.06 to < 0.14",
                ">= 0.14",
            ],
            "Interpretation": [
                "Negligible",
                "Small",
                "Medium",
                "Large",
            ],
        }
    )

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        overview.to_excel(writer, sheet_name="Overview", index=False)
        quality.to_excel(writer, sheet_name="Quality_Effect_Sizes", index=False)
        confidence.to_excel(writer, sheet_name="Confidence_Effect_Sizes", index=False)
        combined.to_excel(writer, sheet_name="Combined_Effect_Sizes", index=False)
        interpretation.to_excel(writer, sheet_name="Interpretation", index=False)

    print("Effect size analysis completed.")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()