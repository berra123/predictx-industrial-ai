import streamlit as st


def show_kpi_cards():

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric(
            "🏭 OEE",
            "89.4%",
            "+2.1%"
        )

    with col2:
        st.metric(
            "⚡ Availability",
            "96.8%",
            "+0.8%"
        )

    with col3:
        st.metric(
            "🤖 AI Risk",
            "82%",
            "-4%"
        )

    with col4:
        st.metric(
            "🚨 Active Alarms",
            "2",
            "-1"
        )

    with col5:
        st.metric(
            "🛠 Work Orders",
            "3",
            "+1"
        )

    with col6:
        st.metric(
            "⚙ Energy",
            "87%",
            "-2%"
        )