import streamlit as st


def show_andon_panel(telemetry, alarm):

    st.subheader("🏭 Hybrid Andon + AI Monitoring")

    if alarm["level"] == "HIGH":
        st.error("🔴 MACHINE CRITICAL")

    elif alarm["level"] == "MEDIUM":
        st.warning("🟡 MAINTENANCE REQUIRED")

    else:
        st.success("🟢 MACHINE RUNNING")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current", f"{telemetry['current']:.1f} A")
        st.metric("Temperature", f"{telemetry['temperature']:.1f} °C")

    with col2:
        st.metric("Vibration", f"{telemetry['vibration']:.2f} mm/s")
        st.metric("Torque", f"{telemetry['torque']:.0f} Nm")
