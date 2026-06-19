import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EV CAN Intrusion Detection System",
    page_icon="🚗",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.metric-container {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚗 EV CAN Intrusion Detection System")
st.markdown("### Real-Time EV Cybersecurity Monitoring Dashboard")

# Load Data
can_df = pd.read_csv("can_data.csv")
attack_df = pd.read_csv("attack_log.csv")

# Metrics
total_messages = len(can_df)
total_attacks = len(attack_df)
avg_speed = round(can_df["Speed"].mean(), 2)
avg_rpm = round(can_df["RPM"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("📡 CAN Messages", total_messages)
col2.metric("🚨 Detected Attacks", total_attacks)
col3.metric("🚘 Average Speed", avg_speed)
col4.metric("⚙ Average RPM", avg_rpm)

# Alert Box
if total_attacks > 0:
    st.error(f"🚨 ALERT: {total_attacks} suspicious CAN messages detected!")
else:
    st.success("✅ No attacks detected")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚘 Vehicle Speed Trend")
    speed_fig = px.line(
        can_df,
        x=can_df.index,
        y="Speed",
        color_discrete_sequence=["#1f77b4"]
    )
    st.plotly_chart(speed_fig, use_container_width=True)

with col2:
    st.subheader("⚙ Vehicle RPM Trend")
    rpm_fig = px.line(
        can_df,
        x=can_df.index,
        y="RPM",
        color_discrete_sequence=["#ff7f0e"]
    )
    st.plotly_chart(rpm_fig, use_container_width=True)

st.markdown("---")

# Attack Distribution
st.subheader("📊 Attack Distribution")

if "Attack_Type" in attack_df.columns:
    attack_counts = attack_df["Attack_Type"].value_counts()

    pie_fig = px.pie(
        values=attack_counts.values,
        names=attack_counts.index,
        hole=0.5,
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    st.plotly_chart(pie_fig, use_container_width=True)

st.markdown("---")

# Data Tables
col1, col2 = st.columns(2)

with col1:
    st.subheader("📡 CAN Data Table")
    st.dataframe(can_df, use_container_width=True)

with col2:
    st.subheader("🚨 Attack Log Table")
    st.dataframe(attack_df, use_container_width=True)

st.markdown("---")

# Downloads
col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "⬇ Download CAN Data",
        can_df.to_csv(index=False),
        file_name="can_data.csv"
    )

with col2:
    st.download_button(
        "⬇ Download Attack Log",
        attack_df.to_csv(index=False),
        file_name="attack_log.csv"
    )

# Sidebar
st.sidebar.title("🔒 Project Information")

st.sidebar.info("""
EV CAN Intrusion Detection System

Features:
✔ Real-Time Monitoring

✔ CAN Traffic Analysis

✔ Speed & RPM Visualization

✔ Attack Detection

✔ Attack Distribution Analysis

✔ Cybersecurity Dashboard
""")

st.sidebar.success("Project Status: Active")
