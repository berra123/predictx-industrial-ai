import streamlit as st
import pandas as pd

from database.alarm_read_repository import get_last_100_alarms


def get_color(level):

    if level == "HIGH":
        return "#C62828"

    elif level == "MEDIUM":
        return "#F9A825"

    return "#2E7D32"


def get_icon(level):

    if level == "HIGH":
        return "🔴"

    elif level == "MEDIUM":
        return "🟡"

    return "🟢"


def show_alarm_card(alarm):

    color = get_color(alarm["alarm_level"])
    icon = get_icon(alarm["alarm_level"])

    st.markdown(
        f"""
<div style="
border-left:8px solid {color};
padding:15px;
margin-bottom:12px;
border-radius:10px;
background-color:#1E1E1E;
">

<h4>{icon} {alarm["alarm_level"]}</h4>

<b>Machine:</b> {alarm["machine"]}<br>

<b>Type:</b> {alarm["alarm_type"]}<br>

<b>Description:</b> {alarm["description"]}<br>

<b>Timestamp:</b> {alarm["timestamp"]}

</div>
""",
        unsafe_allow_html=True
    )


def show_alarms():

    st.title("🚨 Alarm Center")

    st.caption("Real-Time AI Alarm Monitoring")

    alarms = get_last_100_alarms()

    st.divider()

    if len(alarms) == 0:

        st.success("No active alarms.")

        return

    critical = sum(
        1
        for a in alarms
        if a["alarm_level"] == "HIGH"
    )

    warning = sum(
        1
        for a in alarms
        if a["alarm_level"] == "MEDIUM"
    )

    info = sum(
        1
        for a in alarms
        if a["alarm_level"] == "NORMAL"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🔴 Critical",
        critical
    )

    col2.metric(
        "🟡 Warning",
        warning
    )

    col3.metric(
        "🟢 Normal",
        info
    )

    st.divider()

    # ==========================
    # Alarm Cards
    # ==========================

    st.subheader("🚨 Recent Alarms")

    for alarm in reversed(alarms[-10:]):
        show_alarm_card(alarm)

    st.divider()

    # ==========================
    # Alarm History
    # ==========================

    st.subheader("📋 Alarm History")

    df = pd.DataFrame(alarms)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )