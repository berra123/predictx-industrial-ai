import streamlit as st

from components.prediction_history import show_prediction_history
from components.plc_info import show_plc_info
from data_sources.factory_data import get_factory_data

from components.live_charts import show_live_charts
from components.pulper_twin import show_pulper_twin
from components.ai_diagnosis import show_ai_diagnosis
from components.maintenance_panel import show_maintenance_panel
from components.event_timeline import show_event_timeline


def show_pulper():

    factory = get_factory_data()

    telemetry = factory["telemetry"]
    prediction = factory["prediction"]
    alarm = factory["alarm"]

    st.title("🏭 Pulper-03 Digital Twin")

    st.caption("AI Powered Machine Monitoring")

    st.divider()

    # ==========================
    # Machine Status
    # ==========================

    health = prediction["health"]

    if health >= 80:
        st.success("🟢 MACHINE RUNNING")

    elif health >= 50:
        st.warning("🟡 MAINTENANCE REQUIRED")

    else:
        st.error("🔴 CRITICAL CONDITION")

    st.divider()

    left, right = st.columns([2, 1])

    # ==========================
    # Digital Twin
    # ==========================

    with left:

        show_pulper_twin(prediction)

    # ==========================
    # AI Analysis
    # ==========================

    with right:

        st.subheader("🤖 AI Analysis")

        st.metric(
            "Machine Health",
            f"{prediction['health']}%"
        )

        st.metric(
            "Risk Score",
            f"{prediction['risk']}%"
        )

        st.metric(
            "Remaining Life",
            f"{prediction['remaining_life']} Days"
        )

        st.metric(
            "Confidence",
            f"{prediction['confidence']}%"
        )

    st.divider()

    # ==========================
    # PLC Information
    # ==========================

    show_plc_info()

    st.divider()

    # ==========================
    # Live Sensor Values
    # ==========================

    st.subheader("📡 Live Sensor Values")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Current",
            f"{telemetry['current']:.1f} A"
        )

    with col2:
        st.metric(
            "Temperature",
            f"{telemetry['temperature']:.1f} °C"
        )

    with col3:
        st.metric(
            "Vibration",
            f"{telemetry['vibration']:.2f} mm/s"
        )

    with col4:
        st.metric(
            "Torque",
            f"{telemetry['torque']:.1f} Nm"
        )

    with col5:
        st.metric(
            "Speed",
            "1475 RPM"
        )

    st.divider()

    # ==========================
    # AI Recommendation
    # ==========================

    st.subheader("📋 AI Recommendation")

    st.info(
        prediction["recommendation"]
    )

    st.divider()

    # ==========================
    # AI Diagnosis
    # ==========================

    show_ai_diagnosis(
        prediction
    )

    st.divider()

    # ==========================
    # Maintenance Center
    # ==========================

    show_maintenance_panel(
        prediction
    )

    st.divider()

    # ==========================
    # Current Alarm
    # ==========================

    st.subheader("🚨 Current Alarm")

    if alarm["level"] == "NORMAL":

        st.success(
            alarm["description"]
        )

    elif alarm["level"] == "MEDIUM":

        st.warning(
            alarm["description"]
        )

    else:

        st.error(
            alarm["description"]
        )

    st.divider()

    # ==========================
    # Live Trends
    # ==========================

    st.subheader("📈 Live Trends")

    show_live_charts()

    st.divider()

    show_prediction_history()

    st.divider()

    show_event_timeline()