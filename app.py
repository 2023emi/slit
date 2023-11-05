import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import streamlit as st
import yfinance as yf

# Set Streamlit page configuration to full width
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.sidebar.header("Financial Chart")

# Input for selecting a stock symbol
ticker = st.sidebar.text_input("Stock Symbol (e.g., AAPL)", value="AAPL").upper()

# Date range selection
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2022-12-31"))

# Interval selection
intervalv = st.sidebar.text_input("Interval (e.g., '1d' for daily, '1h' for hourly, etc.)", value="1d")

# Fetch data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date, interval=intervalv)

# Check if data is empty
if data.empty:
    st.error("No data available for the selected stock and date range.")
else:
    st.success(f"Data loaded for {ticker} from {start_date} to {end_date}.")

    # Create a StreamlitChart element
    chart = StreamlitChart(width=1099, height=498, toolbox=True)

    # Set the chart data
    chart.set(data)

    # Watermark
    chart.watermark(ticker)

    # Load and display the chart
    chart.load()

    # Add a button to make the chart fullscreen
    if st.button("Fullscreen Chart"):
        # Add CSS to target the iframe with data-testid="stIFrame" and apply a class
        st.markdown("""
        <style>
        iframe[data-testid="stIFrame"] {
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            width: 100%;
            height: 100%;
            border: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            z-index: 999999;
        }
        </style>
        """, unsafe_allow_html=True)

