# ==========================================
# Milestone 1: Import Required Libraries
# ==========================================

import os
import time
import streamlit as st
import pandas as pd
import google.generativeai as genai


# ==========================================
# Milestone 2: Initialize Model
# ==========================================

# Paste your Google API key here
API_KEY = "AIzaSyC-wTF5H0_MjBMhLB-p8zhifY17Z5GWUJs"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")


# ==========================================
# Milestone 3: Prompt Templates
# ==========================================

def get_prompt(prompt_type, data_str):
    if prompt_type == "balance_sheet":
        return f"""
        You are a financial analyst.

        Given the balance sheet data:
        {data_str}

        Provide asset-liability summary, equity position,
        risks and improvement suggestions.
        """
    elif prompt_type == "profit_loss":
        return f"""
        Analyze this profit and loss statement:
        {data_str}

        Provide revenue, margin and profitability insights.
        """
    elif prompt_type == "cash_flow":
        return f"""
        Analyze this cash flow data:
        {data_str}

        Explain operating, investing and financing flows.
        """
    return ""


# ==========================================
# Milestone 4: File Upload and Processing
# ==========================================

def upload_files():
    balance_sheet = st.file_uploader("Upload Balance Sheet", type=["csv", "xlsx"])
    profit_loss = st.file_uploader("Upload Profit and Loss Statement", type=["csv", "xlsx"])
    cash_flow = st.file_uploader("Upload Cash Flow Statement", type=["csv", "xlsx"])
    return balance_sheet, profit_loss, cash_flow


def load_file(file):
    if file is not None:
        if file.name.endswith(".csv"):
            return pd.read_csv(file)
        elif file.name.endswith(".xlsx"):
            return pd.read_excel(file)
    return None


# ==========================================
# Milestone 5: Generate Summary
# ==========================================

def generate_summary(prompt_type, data):

    if data is None:
        return "No data provided."

    data_str = data.to_string()
    prompt = get_prompt(prompt_type, data_str)

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_str = str(e)
        if "429" in error_str:
            st.warning("Rate limit hit, retrying in 15 seconds...")
            time.sleep(15)
            try:
                response = model.generate_content(prompt)
                return response.text
            except Exception as e2:
                return f"Error generating summary: {str(e2)}"
        return f"Error generating summary: {error_str}"


# ==========================================
# Milestone 6: Visualization
# ==========================================

def create_visuals(data, title):
    if data is not None:
        st.subheader(title)
        st.dataframe(data)

        numeric = data.select_dtypes(include=["number"])
        if not numeric.empty:
            st.line_chart(numeric)


# ==========================================
# Milestone 7: Streamlit App Layout
# ==========================================

st.set_page_config(page_title="Gemini Financial Decoder", layout="wide")
st.title("📊 Gemini Financial Decoder")

balance_sheet_file, profit_loss_file, cash_flow_file = upload_files()

if st.button("Generate Reports"):

    with st.spinner("Generating summaries and visualizations..."):

        balance_sheet_data = load_file(balance_sheet_file)
        profit_loss_data = load_file(profit_loss_file)
        cash_flow_data = load_file(cash_flow_file)

        balance_sheet_summary = generate_summary("balance_sheet", balance_sheet_data)
        time.sleep(5)
        profit_loss_summary = generate_summary("profit_loss", profit_loss_data)
        time.sleep(5)
        cash_flow_summary = generate_summary("cash_flow", cash_flow_data)

        st.divider()

        st.subheader("Balance Sheet Summary")
        st.write(balance_sheet_summary)
        create_visuals(balance_sheet_data, "Balance Sheet Data")

        st.divider()

        st.subheader("Profit and Loss Summary")
        st.write(profit_loss_summary)
        create_visuals(profit_loss_data, "Profit and Loss Data")

        st.divider()

        st.subheader("Cash Flow Summary")
        st.write(cash_flow_summary)
        create_visuals(cash_flow_data, "Cash Flow Data")