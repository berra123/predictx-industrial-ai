import streamlit as st
import pandas as pd

from database.alarm_read_repository import get_last_100_alarms


def show_alarms():

    st.title("🚨 Alarm Center")

    st.caption("Real-Time AI Alarm Monitoring")

    alarms = get_last_100_alarms()

    st.divider()

    if len(alarms) == 0:

        st.success("No active alarms.")

        return

    critical = sum(1 for a in alarms if a["alarm_level"] == "HIGH")
    warning = sum(1 for a in alarms if a["alarm_level"] == "MEDIUM")
    info = sum(1 for a in alarms if a["alarm_level"] == "NORMAL")

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

    st.subheader("Alarm History")

    df = pd.DataFrame(alarms)

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )