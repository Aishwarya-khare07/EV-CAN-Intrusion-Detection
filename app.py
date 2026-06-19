import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EV CAN Intrusion Detection System",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 EV CAN Intrusion Detection System")
st.markdown("### Real-Time EV Cybersecurity Monitoring Dashboard")

can_df = pd.read_csv("can_data.csv")
attack_df = pd.read_csv("attack_log.csv")

total_messages = len(can_df)
total_attacks = len(attack_df)
avg_speed = round(can_df["Speed"].mean(), 2)
avg_rpm = round(can_df["RPM"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("CAN Messages", total_messages)
col2.metric("Detected Attacks", total_attacks)
col3.metric("Average Speed", avg_speed)
col4.metric("Average RPM", avg_rpm)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Vehicle Speed")
    fig_speed = px.line(
        can_df,
        x="Time",
        y="Speed",
        title="Speed Trend"
    )
    st.plotly_chart(fig_speed, use_container_width=True)

with col2:
    st.subheader("Vehicle RPM")
    fig_rpm = px.line(
        can_df,
        x="Time",
        y="RPM",
        title="RPM Trend"
    )
    st.plotly_chart(fig_rpm, use_container_width=True)

st.markdown("---")

st.subheader("Attack Distribution")

attack_count = can_df["Attack_Type"].value_counts().reset_index()
attack_count.columns = ["Attack Type", "Count"]

fig_attack = px.pie(
    attack_count,
    names="Attack Type",
    values="Count",
    hole=0.4
)

st.plotly_chart(fig_attack, use_container_width=True)

st.markdown("---")

st.subheader("Attack Log")

st.dataframe(attack_df, use_container_width=True)

st.success("System Status : Monitoring Active")
