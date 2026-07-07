import streamlit as st


def show_maintenance_panel(prediction):

    maintenance = prediction["maintenance"]

    st.subheader("🔧 Maintenance Center")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Priority",
            maintenance["priority"]
        )

        st.metric(
            "Estimated Cost",
            maintenance["estimated_cost"]
        )

        st.metric(
            "Duration",
            maintenance["duration"]
        )

    with col2:

        st.metric(
            "Next Inspection",
            maintenance["next_inspection"]
        )

        st.info(
            maintenance["action"]
        )