import streamlit as st
import pandas as pd
import engine

st.title("Profit Margin Dashboard")

st.header("Upload Files")

sales_file = st.file_uploader("Upload Sales CSV")
ads_file = st.file_uploader("Upload Ads CSV")
refund_file = st.file_uploader("Upload Refund CSV")


if sales_file and ads_file and refund_file:

    result = engine.process_files(
        sales_file,
        ads_file,
        refund_file
    )

    st.header("Results")

    st.write("Revenue:", result["Revenue"])
    st.write("Cost:", result["Cost"])
    st.write("Ads:", result["Ads"])
    st.write("Refunds:", result["Refunds"])
    st.write("Profit:", result["Profit"])
    st.write("Margin %:", result["Margin"])

    st.header("Loss SKUs")

    st.dataframe(result["Loss_SKUs"])