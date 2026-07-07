import streamlit as st


def show_executive_summary(predictions):

    if not predictions:
        st.warning("No prediction data found.")
        return

    latest = predictions[-1]

    left, right = st.columns(2)

    with left:

        st.subheader("🏭 Factory Summary")

        st.success("Factory Running")

        st.metric(
            "Machine",
            "Pulper-03"
        )

        st.metric(
            "Availability",
            "98%"
        )

    with right:

        st.subheader("🤖 AI Summary")

        st.metric(
            "Predicted Failure",
            latest["predicted_failure"]
        )

        st.metric(
            "Remaining Life",
            f"{latest['remaining_life']} Days"
        )

        st.metric(
            "Confidence",
            f"{latest['confidence']}%"
        )