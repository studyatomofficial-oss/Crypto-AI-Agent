from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    output_dir = Path("output")
    csv_path = output_dir / "rolling_summary.csv"

    if not csv_path.exists():
        print(f"Missing file: {csv_path}")
        print("Run at least two scans first so rolling summary data exists.")
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        print("rolling_summary.csv is empty.")
        return

    if "Scan Time" in df.columns:
        df["Scan Time"] = pd.to_datetime(df["Scan Time"], errors="coerce")
        df = df.sort_values("Scan Time")
        x = df["Scan Time"]
        x_label = "Scan Time"
    else:
        x = range(len(df))
        x_label = "Scan Index"

    overlap_col = "Daily Top 25 Overlap"
    if overlap_col not in df.columns:
        print(f"Missing required column: {overlap_col}")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(x, df[overlap_col], marker="o", linewidth=1.8)
    plt.title("Top 25 Overlap Trend")
    plt.xlabel(x_label)
    plt.ylabel("Overlap Count")
    plt.ylim(0, 25)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    overlap_chart = output_dir / "rolling_overlap_trend.png"
    plt.savefig(overlap_chart, dpi=150)
    plt.close()

    contribution_cols = [
        "Avg Funding Score",
        "Avg OI Score",
        "Avg Crowd Score",
        "Avg Base Score",
        "Avg Psychology Score",
    ]
    available_cols = [col for col in contribution_cols if col in df.columns]
    if not available_cols:
        print("No contribution columns found in rolling_summary.csv")
        return

    plt.figure(figsize=(10, 6))
    for col in available_cols:
        plt.plot(x, df[col], marker="o", linewidth=1.8, label=col.replace("Avg ", "").replace(" Score", ""))
    plt.title("Psychology Contribution Trends")
    plt.xlabel(x_label)
    plt.ylabel("Average Score")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    contrib_chart = output_dir / "rolling_contribution_trends.png"
    plt.savefig(contrib_chart, dpi=150)
    plt.close()

    print("Charts generated:")
    print(f"- {overlap_chart}")
    print(f"- {contrib_chart}")


if __name__ == "__main__":
    main()
