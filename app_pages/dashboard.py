import streamlit as st

from data_sources.factory_data import get_factory_data

from components.demo_controller import show_demo_controller
from components.kpi_cards import show_kpi_cards
from components.digital_twin import show_digital_twin
from components.andon_panel import show_andon_panel
from components.ai_prediction import show_ai_prediction
from components.live_charts import show_live_charts


def show_dashboard():

    factory = get_factory_data()

    telemetry = factory["telemetry"]
    prediction = factory["prediction"]
    alarm = factory["alarm"]

    st.title("🏭 PredictX Industrial AI Platform")

    st.caption(
        "AI Powered Predictive Maintenance for Paper Manufacturing"
    )

    st.divider()

    show_demo_controller()

    st.divider()

    show_kpi_cards()

    st.divider()

    show_digital_twin()

    st.divider()

    show_andon_panel(
        telemetry,
        alarm
    )

    st.divider()

    show_ai_prediction(prediction)

    st.divider()

    show_live_charts()