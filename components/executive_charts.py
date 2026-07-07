import streamlit as st
import pandas as pd
import plotly.express as px


def show_executive_charts(predictions, alarms):

    st.subheader("📈 Executive Analytics")

    left, right = st.columns(2)

    with left:

        if predictions:

            df = pd.DataFrame(predictions)

            fig = px.line(
                df,
                x="timestamp",
                y="ai_risk",
                title="AI Risk Trend"
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

    with right:

        if alarms:

            df = pd.DataFrame(alarms)

            fig = px.pie(
                df,
                names="alarm_level",
                title="Alarm Distribution"
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )