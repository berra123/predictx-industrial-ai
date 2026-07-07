import streamlit as st


def show_andon_panel(telemetry):

    st.subheader("🏭 Hybrid Andon + AI Monitoring")

    current = telemetry["current"]
    temperature = telemetry["temperature"]
    vibration = telemetry["vibration"]

    if (
        temperature > 70
        or vibration > 4
        or current > 135
    ):
        st.error("🔴 MACHINE CRITICAL")

    elif (
        temperature > 60
        or vibration > 3
        or current > 120
    ):
        st.warning("🟡 MAINTENANCE REQUIRED")

    else:
        st.success("🟢 MACHINE RUNNING")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current", f"{current:.1f} A")
        st.metric("Temperature", f"{temperature:.1f} °C")

    with col2:
        st.metric("Vibration", f"{vibration:.2f} mm/s")
        st.metric("Torque", f"{telemetry['torque']:.0f} Nm")