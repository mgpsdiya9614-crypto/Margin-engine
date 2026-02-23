import pandas as pd

def process_csv(df):
    df = df.copy()

    # Example profit calculation logic
    if "Revenue" in df.columns and "Cost" in df.columns:
        df["Profit"] = df["Revenue"] - df["Cost"]
        df["Margin %"] = (df["Profit"] / df["Revenue"]) * 100
    else:
        df["Profit"] = "Revenue/Cost columns missing"
        df["Margin %"] = ""

    return df