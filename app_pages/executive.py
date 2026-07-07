import streamlit as st

from database.read_repository import get_last_100_telemetry
from database.prediction_read_repository import get_last_100_predictions
from database.alarm_read_repository import get_last_100_alarms

from components.executive_kpis import show_executive_kpis
from components.executive_summary import show_executive_summary
from components.executive_charts import show_executive_charts
from components.executive_insights import show_executive_insights


def show_executive():

    st.title("📈 Executive Dashboard")

    st.caption("Factory Performance Overview")

    telemetry = get_last_100_telemetry()
    predictions = get_last_100_predictions()
    alarms = get_last_100_alarms()

    st.divider()

    show_executive_kpis(
        telemetry,
        predictions,
        alarms
    )

    st.divider()

    show_executive_summary(
        predictions
    )

    st.divider()

    show_executive_charts(
        predictions,
        alarms
    )

    st.divider()

    show_executive_insights(
        predictions
    )