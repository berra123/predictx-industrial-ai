import streamlit as st


def show_settings():

    st.title("⚙️ Settings")

    st.subheader("🤖 AI Prediction Settings")

    risk_threshold = st.slider(
        "Risk Threshold (%)",
        0,
        100,
        70
    )

    st.divider()

    st.subheader("🚨 Alarm Settings")

    critical_email = st.toggle(
        "Critical Alarm Email Notifications",
        value=True
    )

    auto_shutdown = st.toggle(
        "Automatic Shutdown on Critical Failure",
        value=False
    )

    st.divider()

    st.subheader("📊 Dashboard Settings")

    refresh_rate = st.selectbox(
        "Refresh Interval (seconds)",
        [1, 5, 10, 30, 60],
        index=1
    )

    theme = st.selectbox(
        "Theme",
        [
            "Dark",
            "Light"
        ]
    )

    st.divider()

    st.subheader("🏭 Factory Settings")

    factory_name = st.text_input(
        "Factory Name",
        value="Dentaş Kağıt Sanayi"
    )

    production_line = st.text_input(
        "Default Production Line",
        value="Line A"
    )

    if st.button("💾 Save Settings"):
        st.success("Settings saved successfully.")