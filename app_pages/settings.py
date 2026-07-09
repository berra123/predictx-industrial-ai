import streamlit as st

from database.settings_repository import (
    save_setting,
    get_setting
)


def show_settings():

    st.title("⚙️ Settings")

    # ==================================
    # AI Prediction Settings
    # ==================================
    st.subheader("🤖 AI Prediction Settings")

    risk_threshold = st.slider(
        "Risk Threshold (%)",
        0,
        100,
        int(get_setting("risk_threshold", 70))
    )

    st.divider()

    # ==================================
    # Alarm Settings
    # ==================================
    st.subheader("🚨 Alarm Settings")

    critical_email = st.toggle(
        "Critical Alarm Email Notifications",
        value=get_setting(
            "critical_email",
            "True"
        ) == "True"
    )

    auto_shutdown = st.toggle(
        "Automatic Shutdown on Critical Failure",
        value=get_setting(
            "auto_shutdown",
            "False"
        ) == "True"
    )

    st.divider()

    # ==================================
    # Dashboard Settings
    # ==================================
    st.subheader("📊 Dashboard Settings")

    refresh_options = [1, 5, 10, 30, 60]

    saved_refresh = int(
        get_setting(
            "refresh_rate",
            5
        )
    )

    refresh_rate = st.selectbox(
        "Refresh Interval (seconds)",
        refresh_options,
        index=refresh_options.index(saved_refresh)
    )

    theme_options = [
        "Dark",
        "Light"
    ]

    saved_theme = get_setting(
        "theme",
        "Dark"
    )

    theme = st.selectbox(
        "Theme",
        theme_options,
        index=theme_options.index(saved_theme)
    )

    st.divider()

    # ==================================
    # Factory Settings
    # ==================================
    st.subheader("🏭 Factory Settings")

    factory_name = st.text_input(
        "Factory Name",
        value=get_setting(
            "factory_name",
            "Dentaş Kağıt Sanayi"
        )
    )

    production_line = st.text_input(
        "Default Production Line",
        value=get_setting(
            "production_line",
            "Line A"
        )
    )

    st.divider()

    # ==================================
    # Persisted Settings
    # ==================================
    st.subheader("💾 Persisted Settings")

    email_notifications = st.toggle(
        "Email Notifications",
        value=get_setting(
            "email_notifications",
            "False"
        ) == "True"
    )

    sap_mes_integration = st.toggle(
        "SAP/MES Integration",
        value=get_setting(
            "sap_mes_integration",
            "False"
        ) == "True"
    )

    st.divider()

    # ==================================
    # Save Button
    # ==================================
    if st.button("💾 Save Settings"):

        save_setting(
            "risk_threshold",
            risk_threshold
        )

        save_setting(
            "critical_email",
            critical_email
        )

        save_setting(
            "auto_shutdown",
            auto_shutdown
        )

        save_setting(
            "refresh_rate",
            refresh_rate
        )

        save_setting(
            "theme",
            theme
        )

        save_setting(
            "factory_name",
            factory_name
        )

        save_setting(
            "production_line",
            production_line
        )

        save_setting(
            "email_notifications",
            email_notifications
        )

        save_setting(
            "sap_mes_integration",
            sap_mes_integration
        )

        st.success(
            "Settings saved successfully."
        )