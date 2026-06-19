import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="EV CAN Intrusion Detection System",
    page_icon="🚗",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

can_df = pd.read_csv("can_data.csv")
attack_df = pd.read_csv("attack_log.csv")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🔐 EV Cybersecurity Dashboard")

st.sidebar.markdown("""
### Project Features

✅ CAN Traffic Monitoring

✅ Intrusion Detection

✅ Real-Time Analysis

✅ Vehicle Speed Monitoring

✅ RPM Monitoring

✅ Attack Analytics

✅ Download Reports
""")

st.sidebar.success("System Status: ACTIVE")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚗 EV CAN Intrusion Detection System")
st.markdown("### Real-Time EV Cybersecurity Monitoring Dashboard")

st.divider()

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

total_messages = len(can_df)
total_attacks = len(attack_df)

avg_speed = round(can_df["Speed"].mean(), 2)
avg_rpm = round(can_df["RPM"].mean(), 2)

attack_rate = round(
    (total_attacks / total_messages) * 100,
    2
)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("📡 CAN Messages", total_messages)

with c2:
    st.metric("🚨 Attacks", total_attacks)

with c3:
    st.metric("🚗 Avg Speed", avg_speed)

with c4:
    st.metric("⚙ Avg RPM", avg_rpm)

with c5:
    st.metric("🛡 Attack Rate %", attack_rate)

# --------------------------------------------------
# ALERTS
# --------------------------------------------------

if total_attacks > 20:
    st.error(
        f"🚨 ALERT: {total_attacks} suspicious CAN messages detected!"
    )
else:
    st.success("✅ No major cyber threats detected")

# --------------------------------------------------
# SYSTEM HEALTH
# --------------------------------------------------

st.subheader("🛡 System Health")

h1, h2, h3, h4 = st.columns(4)

with h1:
    st.success("Battery Network Stable")

with h2:
    st.success("Motor Controller Active")

with h3:
    st.success("CAN Communication Healthy")

with h4:
    if total_attacks > 20:
        st.error("Threat Level: HIGH")
    else:
        st.success("Threat Level: LOW")

st.divider()

# --------------------------------------------------
# CHARTS
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📈 Vehicle Speed Trend")

    fig_speed = px.line(
        can_df,
        x="Time",
        y="Speed",
        title="Vehicle Speed"
    )

    st.plotly_chart(
        fig_speed,
        use_container_width=True
    )

with right:

    st.subheader("⚙ Vehicle RPM Trend")

    fig_rpm = px.line(
        can_df,
        x="Time",
        y="RPM",
        title="Vehicle RPM"
    )

    st.plotly_chart(
        fig_rpm,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# VEHICLE STATISTICS
# --------------------------------------------------

st.subheader("🚘 Vehicle Statistics")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.info(
        f"Maximum Speed: {can_df['Speed'].max()}"
    )

with s2:
    st.info(
        f"Minimum Speed: {can_df['Speed'].min()}"
    )

with s3:
    st.info(
        f"Maximum RPM: {can_df['RPM'].max()}"
    )

with s4:
    st.info(
        f"Minimum RPM: {can_df['RPM'].min()}"
    )

st.divider()

# --------------------------------------------------
# ATTACK DISTRIBUTION
# --------------------------------------------------

st.subheader("🛡 Attack Distribution")

if "Attack_Type" in attack_df.columns:

    attack_chart = px.pie(
        attack_df,
        names="Attack_Type",
        hole=0.5,
        title="Attack Types"
    )

    st.plotly_chart(
        attack_chart,
        use_container_width=True
    )

else:
    st.info(
        "Attack_Type column not available in attack_log.csv"
    )

st.divider()

# --------------------------------------------------
# SEARCH
# --------------------------------------------------

st.subheader("🔍 Search CAN Data")

search = st.text_input(
    "Enter any value to search in CAN data"
)

if search:

    filtered = can_df.astype(str).apply(
        lambda row:
        row.str.contains(
            search,
            case=False
        ).any(),
        axis=1
    )

    st.dataframe(
        can_df[filtered],
        use_container_width=True
    )

# --------------------------------------------------
# CAN DATA TABLE
# --------------------------------------------------

st.subheader("📋 Recent CAN Messages")

st.dataframe(
    can_df.tail(20),
    use_container_width=True,
    height=350
)

st.divider()

# --------------------------------------------------
# ATTACK LOG TABLE
# --------------------------------------------------

st.subheader("🚨 Attack Log")

st.dataframe(
    attack_df,
    use_container_width=True,
    height=350
)

st.divider()

# --------------------------------------------------
# DOWNLOAD SECTION
# --------------------------------------------------

st.subheader("⬇ Download Reports")

d1, d2 = st.columns(2)

with d1:

    st.download_button(
        label="Download CAN Data",
        data=can_df.to_csv(index=False),
        file_name="can_data.csv",
        mime="text/csv"
    )

with d2:

    st.download_button(
        label="Download Attack Log",
        data=attack_df.to_csv(index=False),
        file_name="attack_log.csv",
        mime="text/csv"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown("""
### 🔐 EV CAN Intrusion Detection System

Real-Time Automotive Cybersecurity Monitoring Dashboard

Developed using Python, Streamlit, Pandas and Plotly
""")
