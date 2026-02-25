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

    st.write("Revenue:", result["revenue"])
    st.write("Ad Spend:", result["ads"])
    st.write("Refunds:", result["refunds"])
    st.write("Profit:", result["profit"])

    st.subheader("Loss SKUs")

    st.write(result["loss_skus"])


    st.header("Ask Questions")

    question = st.text_input("Ask about your data")

    if question:

        q = question.lower()

        if "profit" in q:
            st.write("Your profit is:", result["profit"])

        elif "revenue" in q:
            st.write("Your revenue is:", result["revenue"])

        elif "refund" in q:
            st.write("Your refunds are:", result["refunds"])

        elif "ads" in q:
            st.write("Your ad spend is:", result["ads"])

        else:
            st.write("I don't understand yet.")