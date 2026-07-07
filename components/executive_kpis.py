import streamlit as st


def show_executive_kpis(
        telemetry,
        predictions,
        alarms
):

    latest = predictions[-1]

    health = 100 - latest["ai_risk"]

    risk = latest["ai_risk"]

    active_alarms = sum(
        1
        for alarm in alarms
        if alarm["alarm_level"] != "NORMAL"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🏭 Factory Health",
        f"{health}%"
    )

    col2.metric(
        "🤖 AI Risk",
        f"{risk}%"
    )

    col3.metric(
        "🚨 Active Alarms",
        active_alarms
    )

    col4.metric(
        "📊 Telemetry",
        len(telemetry)
    )