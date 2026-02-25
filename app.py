import streamlit as st
import engine

st.title("Profit Margin Dashboard")

sales_file = st.file_uploader("Sales CSV")
ads_file = st.file_uploader("Ads CSV")
refund_file = st.file_uploader("Refund CSV")

if sales_file and ads_file and refund_file:

    result = engine.process_files(
        sales_file,
        ads_file,
        refund_file
    )

    st.write(result["Revenue"])
    st.write(result["Cost"])
    st.write(result["Ads"])
    st.write(result["Refunds"])
    st.write(result["Profit"])
    st.write(result["Margin"])

    st.dataframe(result["Loss_SKUs"])