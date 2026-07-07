import streamlit as st
import pandas as pd

from database.read_repository import get_last_100_telemetry
from database.alarm_read_repository import get_last_100_alarms
from database.prediction_read_repository import get_last_100_predictions


def show_reports():

    st.title("📊 Reports")

    st.caption("Production Analytics & AI Reports")

    telemetry = get_last_100_telemetry()
    predictions = get_last_100_predictions()
    alarms = get_last_100_alarms()

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Telemetry",
        len(telemetry)
    )

    col2.metric(
        "Predictions",
        len(predictions)
    )

    col3.metric(
        "Alarms",
        len(alarms)
    )

    st.divider()

    st.subheader("📡 Telemetry History")

    if telemetry:

        df = pd.DataFrame(telemetry)

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )

    else:

        st.info("No telemetry data found.")

    st.divider()

    st.subheader("🤖 AI Prediction History")

    if predictions:

        df = pd.DataFrame(predictions)

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )

    else:

        st.info("No prediction records found.")

    st.divider()

    st.subheader("🚨 Alarm History")

    if alarms:

        df = pd.DataFrame(alarms)

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )

    else:

        st.info("No alarm records found.")