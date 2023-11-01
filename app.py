
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
from datetime import datetime, timezone, timedelta
import streamlit as st

chart = StreamlitChart(width=1099, height=498)  # Set the desired width and height

df = pd.read_csv('ohlcv.csv')
# Columns: time | open | high | low | close | volume
# Convert the 'timestamp' column to a datetime object
# df['timestamp'] = pd.to_datetime(df['timestamp'])
# Rename columns to match lightweight-charts requirements
df = df.rename(columns={'timestamp': 'time', 'open': 'open', 'high': 'high', 'low': 'low', 'close': 'close', 'volume': 'volume'})
# Convert the 'time' column to a datetime object
df['time'] = pd.to_datetime(df['time'])
# Convert the 'time' column to UTC by subtracting the UTC offset (5 hours and 30 minutes)
df['time'] = df['time'] + timedelta(hours=5, minutes=30)


chart.set(df)



# Set Streamlit page configuration to full width
st.set_page_config(layout="wide")

# Add the CSS code to hide the deploy button
st.markdown("""
  <style>
    .stDeployButton {
      display: none;
    }
  </style>
""", unsafe_allow_html=True)



# Add a centered div around the chart
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
      <div class="centered-chart">
    """,
    unsafe_allow_html=True,  # Allow raw HTML to be rendered
)

# Load and display the chart
chart.load()

# Close the centered div
st.markdown(
    """
      </div>
    </div>
    """,
    unsafe_allow_html=True,  # Allow raw HTML to be rendered
)


