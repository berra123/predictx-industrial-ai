import streamlit as st


def render_sidebar():

    st.sidebar.title("🏭 PredictX")
    st.sidebar.caption(
        "AI Powered Predictive Maintenance"
    )

    st.sidebar.divider()

    page = st.sidebar.radio(
        "📂 Navigation",
        [
            "📈 Dashboard",
            "🏭 Pulper",
            "🚨 Alarm Center",
            "🛠 Work Orders",
            "📊 Reports",
            "⚙️ Settings"
        ]
    )

    st.sidebar.divider()

    st.sidebar.subheader("🏭 Production Status")

    st.sidebar.success("🟢 Pulper")
    st.sidebar.success("🟢 Paper Machine")
    st.sidebar.warning("🟡 Corrugator")
    st.sidebar.error("🔴 Compressor")

    st.sidebar.divider()

    st.sidebar.subheader("🤖 AI System")

    st.sidebar.metric(
        "AI Health",
        "98.7%",
        "+0.4%"
    )

    st.sidebar.metric(
        "Model Version",
        "v1.0"
    )

    st.sidebar.metric(
        "Prediction Accuracy",
        "94.2%"
    )

    st.sidebar.divider()

    st.sidebar.caption(
        "PredictX Industrial AI Platform"
    )

    st.sidebar.caption(
        "Version 1.0"
    )

    return page