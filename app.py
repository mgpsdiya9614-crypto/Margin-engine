import streamlit as st
from engine import process_files

st.set_page_config(
    page_title="Margin Engine",
    layout="wide"
)

st.title("📊 Weekly Contribution Margin Engine")

st.markdown(
"""
Upload your weekly CSV files to calculate real profit clarity.
"""
)

# Uploaders

st.subheader("Upload Files")

sales_file = st.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

ads_file = st.file_uploader(
    "Upload Ads CSV",
    type=["csv"]
)

refunds_file = st.file_uploader(
    "Upload Refunds CSV",
    type=["csv"]
)

cogs_file = st.file_uploader(
    "Upload COGS CSV",
    type=["csv"]
)

# Run engine

if st.button("Calculate Profit"):

    if sales_file and ads_file and refunds_file and cogs_file:

        try:

            summary, full_data, loss_skus = process_files(
                sales_file,
                ads_file,
                refunds_file,
                cogs_file
            )

            st.subheader("📌 Summary")

            col1, col2, col3, col4, col5 = st.columns(5)

            col1.metric(
                "Revenue",
                f"₹{summary['Total Revenue']}"
            )

            col2.metric(
                "Ad Spend",
                f"₹{summary['Total Ad Spend']}"
            )

            col3.metric(
                "Refunds",
                f"₹{summary['Total Refunds']}"
            )

            col4.metric(
                "COGS",
                f"₹{summary['Total COGS']}"
            )

            col5.metric(
                "Contribution Margin",
                f"₹{summary['Contribution Margin']}"
            )


            st.subheader("📦 SKU Breakdown")

            st.dataframe(
                full_data,
                use_container_width=True
            )


            st.subheader("⚠ Loss Making SKUs")

            if loss_skus.empty:

                st.success(
                    "No loss making SKUs"
                )

            else:

                st.dataframe(
                    loss_skus,
                    use_container_width=True
                )


        except Exception as e:

            st.error(f"Error: {e}")

    else:

        st.warning(
            "Upload all 4 files"
        )