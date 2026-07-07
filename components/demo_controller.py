import streamlit as st

from models.scenario_engine import scenario
from data_sources.history_buffer import clear_history


def show_demo_controller():

    st.subheader("🎬 Demo Controller")

    # Durum bilgisi
    if scenario.is_running():
        st.success("Status : 🟢 RUNNING")
    else:
        st.info("Status : ⏸ PAUSED")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "▶ Start Demo",
            use_container_width=True
        ):
            scenario.start()

    with col2:

        if st.button(
            "⏸ Pause",
            use_container_width=True
        ):
            scenario.pause()

    with col3:

        if st.button(
            "🔄 Reset",
            use_container_width=True
        ):
            scenario.reset()
            clear_history()

            st.success("Demo reset successfully.")