import streamlit as st


def show_ai_prediction(prediction):

    st.subheader("🤖 AI Prediction Center")

    risk = prediction["risk"]

    if risk < 40:
        st.success("🟢 Healthy")

    elif risk < 70:
        st.warning("🟡 Maintenance Recommended")

    else:
        st.error("🔴 High Failure Risk")

    st.metric(
        "AI Risk Score",
        f"{risk}%"
    )

    st.write(f"**Predicted Failure:** {prediction['failure']}")
    st.write(f"**Remaining Useful Life:** {prediction['remaining_life']} Days")
    st.write(f"**Confidence:** {prediction['confidence']}%")
    st.write(f"**Recommendation:** {prediction['recommendation']}")