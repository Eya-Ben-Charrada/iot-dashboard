import streamlit as st
import pandas as pd
import sqlite3
from io import StringIO
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="🌡️ IoT Dashboard: Temperature & Light", layout="wide")

DB_PATH = "C:/Users/THINKPAD/Documents/serial_mqtt/sensor_data.db"

def load_data(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT timestamp, temperature, light FROM sensor_readings
        WHERE timestamp BETWEEN ? AND ?
        ORDER BY timestamp
    """
    df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    conn.close()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def stats(df, col):
    return {
        "min": df[col].min(),
        "max": df[col].max(),
        "avg": df[col].mean()
    }

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

st.title("🌡️ IoT Dashboard: Temperature & Light")

with st.sidebar:
    st.header("Settings")
    
    # Date filter inputs
    today = datetime.now()
    default_start = (today - timedelta(days=7)).date()
    default_end = today.date()
    
    start_date = st.date_input("Start date", value=default_start, max_value=today.date())
    end_date = st.date_input("End date", value=default_end, max_value=today.date())
    
    if start_date > end_date:
        st.error("Error: Start date must be before End date.")
    
    refresh_seconds = st.number_input("Auto-refresh every (seconds)", min_value=5, max_value=300, value=15, step=5)
    
    temp_threshold = st.number_input("Temperature alert threshold (°C)", min_value=-50.0, max_value=150.0, value=40.0, step=0.1)

# Convert dates to string timestamps
start_dt_str = datetime.combine(start_date, datetime.min.time()).strftime("%Y-%m-%d %H:%M:%S")
end_dt_str = datetime.combine(end_date, datetime.max.time()).strftime("%Y-%m-%d %H:%M:%S")

# Load data filtered by date range
df = load_data(start_dt_str, end_dt_str)

if df.empty:
    st.warning("No data available for the selected date range.")
else:
    # Show latest readings as metrics
    latest_temp = df['temperature'].iloc[-1]
    latest_light = df['light'].iloc[-1]
    
    col1, col2 = st.columns(2)
    col1.metric("Latest Temperature (°C)", f"{latest_temp:.2f}")
    col2.metric("Latest Light Level", f"{latest_light}")
    
    # Show alert if temperature exceeds threshold
    if latest_temp > temp_threshold:
        st.error(f"⚠️ Alert: Temperature {latest_temp:.2f}°C exceeded threshold of {temp_threshold}°C!")
    
    # Statistics
    st.subheader("Statistics")
    stats_temp = stats(df, 'temperature')
    stats_light = stats(df, 'light')
    
    stats_col1, stats_col2 = st.columns(2)
    
    with stats_col1:
        st.markdown("**Temperature (°C)**")
        st.write(f"Min: {stats_temp['min']:.2f}")
        st.write(f"Max: {stats_temp['max']:.2f}")
        st.write(f"Average: {stats_temp['avg']:.2f}")
        
    with stats_col2:
        st.markdown("**Light Level**")
        st.write(f"Min: {stats_light['min']}")
        st.write(f"Max: {stats_light['max']}")
        st.write(f"Average: {stats_light['avg']:.2f}")
    
    # Charts
    st.subheader("🌡 Temperature Over Time")
    st.line_chart(data=df.set_index('timestamp')['temperature'])
    
    st.subheader("💡 Light Level Over Time")
    st.line_chart(data=df.set_index('timestamp')['light'])
    
    # CSV Export
    csv_data = convert_df_to_csv(df)
    st.download_button(
        label=" ⬇️ Download data as CSV",
        data=csv_data,
        file_name=f"sensor_data_{start_date}_{end_date}.csv",
        mime="text/csv",
        key="download_csv_button"
    )

# Auto-refresh logic
time.sleep(refresh_seconds)
st.rerun()
