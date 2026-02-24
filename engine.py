import pandas as pd

def analyze_margin(df):

    report = {}

    if "Revenue" in df.columns and "Cost" in df.columns:

        total_revenue = df["Revenue"].sum()
        total_cost = df["Cost"].sum()

        profit = total_revenue - total_cost

        if total_revenue > 0:
            margin = (profit / total_revenue) * 100
        else:
            margin = 0

        report["Total Revenue"] = total_revenue
        report["Total Cost"] = total_cost
        report["Profit"] = profit
        report["Margin %"] = round(margin,2)

    else:

        report["Error"] = "Columns Revenue and Cost required"

    return report