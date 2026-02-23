import pandas as pd

def validate_columns(df, required_columns):
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

def process_files(sales_file, ads_file, refunds_file, cogs_file):
    sales = pd.read_csv(sales_file)
    ads = pd.read_csv(ads_file)
    refunds = pd.read_csv(refunds_file)
    cogs = pd.read_csv(cogs_file)

    # Standardize column names
    sales.columns = sales.columns.str.strip().str.lower()
    ads.columns = ads.columns.str.strip().str.lower()
    refunds.columns = refunds.columns.str.strip().str.lower()
    cogs.columns = cogs.columns.str.strip().str.lower()

    # Validate required columns
    validate_columns(sales, ["sku", "revenue"])
    validate_columns(ads, ["sku", "ad_spend"])
    validate_columns(refunds, ["sku", "refund_amount"])
    validate_columns(cogs, ["sku", "cost_of_goods"])

    # Aggregate revenue per SKU
    sales_summary = sales.groupby("sku")["revenue"].sum().reset_index()

    # Merge all datasets
    data = sales_summary.merge(ads, on="sku", how="left")
    data = data.merge(refunds, on="sku", how="left")
    data = data.merge(cogs, on="sku", how="left")

    data.fillna(0, inplace=True)

    # Calculate Contribution Margin
    data["contribution_margin"] = (
        data["revenue"]
        - data["ad_spend"]
        - data["refund_amount"]
        - data["cost_of_goods"]
    )

    total_summary = {
        "Total Revenue": round(data["revenue"].sum(), 2),
        "Total Ad Spend": round(data["ad_spend"].sum(), 2),
        "Total Refunds": round(data["refund_amount"].sum(), 2),
        "Total COGS": round(data["cost_of_goods"].sum(), 2),
        "Contribution Margin": round(data["contribution_margin"].sum(), 2),
    }

    loss_skus = data[data["contribution_margin"] < 0]

    return total_summary, data, loss_skus