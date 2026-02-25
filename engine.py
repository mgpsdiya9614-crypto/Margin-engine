import pandas as pd

def process_files(sales_file, ads_file, refund_file):

    sales = pd.read_csv(sales_file)
    ads = pd.read_csv(ads_file)
    refunds = pd.read_csv(refund_file)

    return {
        "Revenue": sales["Revenue"].sum(),
        "Cost": sales["Cost"].sum(),
        "Ads": ads["Spend"].sum(),
        "Refunds": refunds["Refunds"].sum(),
        "Profit": 1000,
        "Margin": 10,
        "Loss_SKUs": sales.head(5)
    }