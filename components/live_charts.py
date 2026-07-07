import streamlit as st
import plotly.graph_objects as go

from database.read_repository import get_last_100_telemetry


def create_chart(title, values, color):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=values,
            mode="lines",
            line=dict(color=color, width=3)
        )
    )

    fig.update_layout(

        title=title,

        height=260,

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        template="plotly_dark",

        xaxis_title="",

        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_live_charts():

    history = get_last_100_telemetry()

    if len(history) < 2:
        st.info("Waiting for telemetry history...")
        return

    st.subheader("📈 Live Telemetry")

    current = [x["current"] for x in history]
    temperature = [x["temperature"] for x in history]
    vibration = [x["vibration"] for x in history]
    torque = [x["torque"] for x in history]

    col1, col2 = st.columns(2)

    with col1:

        create_chart(
            "⚡ Current",
            current,
            "#00E676"
        )

        create_chart(
            "📳 Vibration",
            vibration,
            "#29B6F6"
        )

    with col2:

        create_chart(
            "🌡 Temperature",
            temperature,
            "#FFA726"
        )

        create_chart(
            "⚙ Torque",
            torque,
            "#AB47BC"
        )