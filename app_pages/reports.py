import streamlit as st
import pandas as pd
import plotly.express as px

from database.read_repository import get_last_100_telemetry
from database.prediction_read_repository import get_last_100_predictions
from database.alarm_read_repository import get_last_100_alarms


def show_reports():

    st.title("📊 Reports")

    st.caption("Production Analytics Dashboard")

    telemetry = get_last_100_telemetry()
    predictions = get_last_100_predictions()
    alarms = get_last_100_alarms()

    if not telemetry:
        st.warning("No telemetry data found.")
        return

    df = pd.DataFrame(telemetry)
    pred_df = pd.DataFrame(predictions)
    alarm_df = pd.DataFrame(alarms)

    # =====================
    # KPI CARDS
    # =====================

    avg_risk = (
        pred_df["ai_risk"].mean()
        if not pred_df.empty
        else 0
    )

    avg_health = 100 - avg_risk

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Factory Health",
            f"{avg_health:.1f}%"
        )

    with col2:
        st.metric(
            "Average AI Risk",
            f"{avg_risk:.1f}%"
        )

    with col3:
        st.metric(
            "Predictions",
            len(pred_df)
        )

    with col4:
        st.metric(
            "Alarms",
            len(alarm_df)
        )

    st.divider()

    # =====================
    # AI ANALYTICS
    # =====================

    st.subheader("🤖 AI Analytics")

    left, right = st.columns(2)

    with left:

        if not pred_df.empty:

            fig = px.line(
                pred_df,
                x="timestamp",
                y="ai_risk",
                title="AI Risk Trend"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with right:

        if not alarm_df.empty:

            fig = px.pie(
                alarm_df,
                names="alarm_level",
                title="Alarm Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.divider()

    # =====================
    # TELEMETRY TRENDS
    # =====================

    st.subheader("📈 Telemetry Trends")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.line(
            df,
            x="timestamp",
            y="temperature",
            title="Temperature Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        fig = px.line(
            df,
            x="timestamp",
            y="current",
            title="Current Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.line(
            df,
            x="timestamp",
            y="vibration",
            title="Vibration Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        fig = px.line(
            df,
            x="timestamp",
            y="torque",
            title="Torque Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # =====================
    # PREDICTION HISTORY
    # =====================

    if not pred_df.empty:

        st.subheader("🤖 Prediction History")

        st.dataframe(
            pred_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

    # =====================
    # ALARM HISTORY
    # =====================

    if not alarm_df.empty:

        st.subheader("🚨 Alarm History")

        st.dataframe(
            alarm_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

    # =====================
    # TELEMETRY HISTORY
    # =====================

    st.subheader("📋 Telemetry History")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )