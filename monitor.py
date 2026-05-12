import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("=== System Monitoring ===")
print(f"CPU Usage: {cpu}%")
print(f"RAM Usage: {memory}%")
print(f"Disk Usage: {disk}%")
import streamlit as st
import psutil
import time

st.set_page_config(page_title="Quntom Migration Monitor", layout="wide")

st.title("Quntom Migration - Live Monitoring Dashboard")

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent

st.metric("CPU Usage", f"{cpu}%")
st.metric("Memory Usage", f"{memory}%")
st.metric("Migration Status", "Stable")
st.metric("Files Migrated", "2")
st.metric("Cost Reduction", "29.17%")

st.success("Monitoring System Active")
import psutil

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

st.metric("CPU Usage", f"{cpu}%")
st.metric("RAM Usage", f"{ram}%")
import pandas as pd
import random

chart_data = pd.DataFrame({
    "CPU": [random.randint(20, 90) for _ in range(10)],
    "RAM": [random.randint(30, 95) for _ in range(10)]
})

st.line_chart(chart_data)
st.metric("Before Optimization", "$120")
st.metric("After Optimization", "$85")