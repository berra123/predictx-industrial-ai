import streamlit as st


def show_ai_prediction(prediction):

    st.subheader("🤖 AI Prediction Center")

    risk = prediction["risk"]
    health = prediction["health"]

    # Alarm Durumu
    if risk < 30:
        st.success("🟢 Healthy")

    elif risk < 60:
        st.warning("🟡 Inspection Required")

    elif risk < 80:
        st.warning("🟠 Maintenance Required")

    else:
        st.error("🔴 Critical Failure")

    # Health Bar
    st.write("### 🩺 Machine Health")

    st.progress(health / 100)

    st.metric(
        "Health Score",
        f"{health}%"
    )

    st.metric(
        "AI Risk Score",
        f"{risk}%"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Remaining Life",
            f"{prediction['remaining_life']} Days"
        )

        st.metric(
            "Confidence",
            f"{prediction['confidence']}%"
        )

    with col2:
        st.write("**Predicted Failure**")
        st.info(prediction["failure"])

        st.write("**Recommendation**")
        st.success(prediction["recommendation"])