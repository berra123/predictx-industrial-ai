import streamlit as st
import pandas as pd
from database.alarm_read_repository import get_last_100_alarms


def get_color(level):
    if level == "CRITICAL":
        return "#B71C1C"
    elif level == "HIGH":
        return "#E65100"
    elif level == "MEDIUM":
        return "#F9A825"
    return "#2E7D32"


def get_icon(level):
    if level == "CRITICAL":
        return "🚨"
    elif level == "HIGH":
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
            <h4>{icon} {alarm["alarm_level"]} - {alarm["alarm_type"]}</h4>

            <b>Machine:</b> {alarm["machine"]}<br>
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

    # ==========================
    # Metrics
    # ==========================

    critical = sum(
        1 for a in alarms
        if a["alarm_level"] == "CRITICAL"
    )

    high = sum(
        1 for a in alarms
        if a["alarm_level"] == "HIGH"
    )

    medium = sum(
        1 for a in alarms
        if a["alarm_level"] == "MEDIUM"
    )

    normal = sum(
        1 for a in alarms
        if a["alarm_level"] == "NORMAL"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🚨 Critical",
        critical
    )

    col2.metric(
        "🔴 High",
        high
    )

    col3.metric(
        "🟡 Warning",
        medium
    )

    col4.metric(
        "🟢 Normal",
        normal
    )

    st.divider()

    # ==========================
    # Filters
    # ==========================

    st.subheader("🔍 Alarm Filters")

    f_col1, f_col2 = st.columns(2)

    with f_col1:
        selected_level = st.selectbox(
            "Alarm Level",
            [
                "ALL",
                "CRITICAL",
                "HIGH",
                "MEDIUM",
                "NORMAL"
            ]
        )

    with f_col2:
        machines = ["ALL"] + sorted(
            list(
                set(
                    a["machine"]
                    for a in alarms
                )
            )
        )

        selected_machine = st.selectbox(
            "Machine",
            machines
        )

    # ==========================
    # Filtering
    # ==========================

    filtered_alarms = alarms

    if selected_level != "ALL":
        filtered_alarms = [
            a for a in filtered_alarms
            if a["alarm_level"] == selected_level
        ]

    if selected_machine != "ALL":
        filtered_alarms = [
            a for a in filtered_alarms
            if a["machine"] == selected_machine
        ]

    st.divider()

    # ==========================
    # Recent Alarms
    # ==========================

    st.subheader("🚨 Recent Alarms")

    if len(filtered_alarms) == 0:
        st.info(
            "No alarms match the selected filters."
        )
    else:
        for alarm in reversed(filtered_alarms[-10:]):
            show_alarm_card(alarm)

    st.divider()

    # ==========================
    # Alarm History
    # ==========================

    st.subheader("📋 Alarm History")

    if len(filtered_alarms) > 0:

        df = pd.DataFrame(filtered_alarms)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info(
            "No history data to display for current filters."
        )