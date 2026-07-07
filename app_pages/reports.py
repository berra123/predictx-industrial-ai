import streamlit as st
import pandas as pd
import plotly.express as px

from database.read_repository import get_last_100_telemetry


def show_reports():

    st.title("📊 Reports")

    st.caption("Production Analytics Dashboard")

    telemetry = get_last_100_telemetry()

    if not telemetry:
        st.warning("No telemetry data found.")
        return

    df = pd.DataFrame(telemetry)

    # =====================
    # KPI CARDS
    # =====================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Telemetry Records",
        len(df)
    )

    col2.metric(
        "Average Temperature",
        f"{df['temperature'].mean():.1f} °C"
    )

    col3.metric(
        "Average Current",
        f"{df['current'].mean():.1f} A"
    )

    st.divider()

    st.subheader("📈 Telemetry Trends")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.line(
            df,
            x="timestamp",
            y="temperature",
            title="Temperature"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        fig = px.line(
            df,
            x="timestamp",
            y="current",
            title="Current"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with col2:

        fig = px.line(
            df,
            x="timestamp",
            y="vibration",
            title="Vibration"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        fig = px.line(
            df,
            x="timestamp",
            y="torque",
            title="Torque"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    st.divider()

    st.subheader("📋 Telemetry History")

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )