import streamlit as st

from data_sources.factory_data import get_factory_data

from components.factory_overview import show_factory_overview
from components.demo_controller import show_demo_controller
from components.kpi_cards import show_kpi_cards
from components.digital_twin import show_digital_twin
from components.andon_panel import show_andon_panel
from components.ai_prediction import show_ai_prediction
from components.live_charts import show_live_charts
from components.event_timeline import show_event_timeline


def show_dashboard():

    factory = get_factory_data()

    telemetry = factory["telemetry"]
    prediction = factory["prediction"]
    alarm = factory["alarm"]

    st.title("🏭 PredictX Industrial AI Platform")

    st.caption(
        "AI Powered Predictive Maintenance for Paper Manufacturing"
    )

    # =====================================
    # Factory Overview
    # =====================================

    show_factory_overview(
        prediction
    )

    st.divider()

    # =====================================
    # Demo Controller
    # =====================================

    show_demo_controller()

    st.divider()

    # =====================================
    # KPI Cards
    # =====================================

    show_kpi_cards()

    st.divider()

    # =====================================
    # Digital Twin
    # =====================================

    show_digital_twin()

    st.divider()

    # =====================================
    # Hybrid Andon Panel
    # =====================================

    show_andon_panel(
        telemetry,
        alarm
    )

    st.divider()

    # =====================================
    # AI Prediction Center
    # =====================================

    show_ai_prediction(
        prediction
    )

    st.divider()

    # =====================================
    # Live Trends
    # =====================================

    st.subheader("📈 Live Factory Trends")

    show_live_charts()

    st.divider()

    # =====================================
    # Event Timeline
    # =====================================

    show_event_timeline()