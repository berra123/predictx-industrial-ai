import streamlit as st

from data_sources.factory_data import get_factory_data

from components.demo_controller import show_demo_controller
from components.kpi_cards import show_kpi_cards
from components.digital_twin import show_digital_twin
from components.andon_panel import show_andon_panel
from components.ai_prediction import show_ai_prediction
from components.live_charts import show_live_charts


def show_dashboard():

    # Veri Katmanı
    factory = get_factory_data()

    telemetry = factory["telemetry"]
    prediction = factory["prediction"]
    alarm = factory["alarm"]

    st.title("🏭 PredictX Industrial AI Platform")

    st.caption(
        "AI Powered Predictive Maintenance for Paper Manufacturing"
    )

    st.divider()

    # Demo Controller
    show_demo_controller()

    st.divider()

    # KPI Kartları
    show_kpi_cards()

    st.divider()

    # Dijital Üretim Hattı
    show_digital_twin()

    st.divider()

    # Hibrit Andon Paneli
    show_andon_panel(telemetry)

    st.divider()

    # AI Prediction Center
    show_ai_prediction(prediction)

    st.divider()

    # Canlı Telemetri Grafikleri
    show_live_charts()