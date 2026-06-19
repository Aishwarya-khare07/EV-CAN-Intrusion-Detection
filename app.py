import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="EV CAN Intrusion Detection System",
    page_icon="🚗",
    layout="wide"
)

# ---------------- CUSTOM THEME ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b,#312e81);
    color:white;
}

h1,h2,h3 {
    color:white !important;
}

[data-testid="metric-container"] {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.3);
}

[data-testid="metric-container"] label {
    color:white !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#1e3a8a,#2563eb,#7c3aed);
}

div[data-testid="stPlotlyChart"] {
    background:white;
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #

can_df = pd.read_csv("can_data.csv")
attack_df = pd.read_csv("attack_log.csv")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🔐 Project Information")

st.sidebar.info("""
EV CAN Intrusion Detection

✔ Real-Time Monitoring

✔ CAN Traffic Analysis

✔ Speed & RPM Visualization

✔ Attack Detection

✔ Attack Distribution Analysis

✔ Cybersecurity Dashboard
""")

st.sidebar.success("Status: Active")

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='text-align:center;'>
🚗 EV CAN Intrusion Detection System
</h1>

<h3 style='text-align:center;color:#93c5fd;'>
Real-Time EV Cybersecurity Monitoring Dashboard
</h3>
""", unsafe_allow_html=True)

# ---------------- METRICS ---------------- #

total_messages = len(can_df)
total_attacks = len(attack_df)

avg_speed = round(can_df["Speed"].mean(),2)
avg_rpm = round(can_df["RPM"].mean(),2)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("📡 CAN Messages", total_messages)

with c2:
    st.metric("🚨 Detected Attacks", total_attacks)

with c3:
    st.metric("🚗 Average Speed", avg_speed)

with c4:
    st.metric("⚙ Average RPM", avg_rpm)

# ---------------- ALERT ---------------- #

if total_attacks > 0:
    st.error(f"🚨 ALERT: {total_attacks} suspicious CAN messages detected!")
else:
    st.success("✅ System Secure - No attacks detected")

st.divider()

# ---------------- SPEED & RPM GRAPHS ---------------- #

col1,col2 = st.columns(2)

with col1:

    st.subheader("📈 Vehicle Speed Trend")

    fig_speed = px.line(
        can_df,
        x="Time",
        y="Speed",
        title="Speed Trend"
    )

    fig_speed.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig_speed,use_container_width=True)

with col2:

    st.subheader("⚙ Vehicle RPM Trend")

    fig_rpm = px.line(
        can_df,
        x="Time",
        y="RPM",
        title="RPM Trend"
    )

    fig_rpm.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig_rpm,use_container_width=True)

st.divider()

# ---------------- ATTACK DISTRIBUTION ---------------- #

st.subheader("🛡 Attack Distribution")

if "Attack_Type" in attack_df.columns:

    fig_attack = px.pie(
        attack_df,
        names="Attack_Type",
        hole=0.5,
        title="Attack Distribution"
    )

    st.plotly_chart(fig_attack,use_container_width=True)

else:

    st.info("Attack_Type column not found in attack_log.csv")

st.divider()

# ---------------- CAN DATA TABLE ---------------- #

st.subheader("📋 Recent CAN Messages")

st.dataframe(
    can_df.tail(15),
    use_container_width=True
)

st.divider()

# ---------------- ATTACK LOG TABLE ---------------- #

st.subheader("🚨 Attack Log")

st.dataframe(
    attack_df,
    use_container_width=True
)

st.divider()

# ---------------- FOOTER ---------------- #

st.markdown("""
<center>

### 🔐 EV Cybersecurity Dashboard

Developed for EV CAN Bus Intrusion Detection & Monitoring

</center>
""", unsafe_allow_html=True)
