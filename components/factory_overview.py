import streamlit as st

from database.dashboard_repository import get_dashboard_statistics


def show_factory_overview(prediction):

    stats = get_dashboard_statistics()

    health = prediction["health"]

    if health >= 80:
        status = "🟢 RUNNING"

    elif health >= 50:
        status = "🟡 WARNING"

    else:
        status = "🔴 CRITICAL"

    st.subheader("🏭 Factory Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Factory Status",
        status
    )

    col2.metric(
        "Machines",
        stats["machines"]
    )

    col3.metric(
        "Telemetry",
        stats["telemetry"]
    )

    col4.metric(
        "Alarms",
        stats["alarms"]
    )

    col5.metric(
        "Average Risk",
        f"{stats['avg_risk']}%"
    )