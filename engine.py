import pandas as pd

def process_files(sales_file, ads_file, refund_file):

    sales = pd.read_csv(sales_file)
    ads = pd.read_csv(ads_file)
    refunds = pd.read_csv(refund_file)

    total_revenue = sales["Revenue"].sum()
    total_cost = sales["Cost"].sum()
    ad_spend = ads["Spend"].sum()
    refund_total = refunds["Refunds"].sum()

    profit = total_revenue - total_cost - ad_spend - refund_total

    margin = 0
    if total_revenue != 0:
        margin = (profit / total_revenue) * 100

    sales["Profit"] = sales["Revenue"] - sales["Cost"]

    loss_skus = sales[sales["Profit"] < 0]

    return {
        "Revenue": total_revenue,
        "Cost": total_cost,
        "Ads": ad_spend,
        "Refunds": refund_total,
        "Profit": profit,
        "Margin": margin,
        "Loss_SKUs": loss_skus
    }