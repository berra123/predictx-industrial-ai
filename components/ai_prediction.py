import streamlit as st

from services.ml_prediction_service import predict_failure


def show_ai_prediction(prediction, telemetry):

    st.subheader("🤖 AI Prediction Center")

    # ==========================
    # ML Prediction
    # ==========================

    ml_prediction, probability = predict_failure(
        current=telemetry["current"],
        temperature=telemetry["temperature"],
        vibration=telemetry["vibration"],
        torque=telemetry["torque"],
        speed=telemetry["speed"]
    )

    risk = round(probability * 100, 1)
    health = max(0, 100 - int(risk))

    # Predicted Failure
    if ml_prediction == 1:

        if telemetry["vibration"] > 4.5:
            failure = "Bearing Failure"

        elif telemetry["temperature"] > 90:
            failure = "Motor Overheating"

        elif telemetry["current"] > 420:
            failure = "Overcurrent Condition"

        else:
            failure = "Potential Failure"

    else:
        failure = "No Failure Detected"

    # Recommendation
    if risk < 30:
        recommendation = "Machine operating within normal limits."

    elif risk < 60:
        recommendation = "Schedule inspection during next maintenance window."

    elif risk < 80:
        recommendation = "Maintenance intervention recommended."

    else:
        recommendation = "Immediate maintenance action required."

    # Alarm Status
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

        remaining_life = max(
            1,
            int((100 - risk) * 0.8)
        )

        st.metric(
            "Remaining Life",
            f"{remaining_life} Days"
        )

        st.metric(
            "Confidence",
            f"{risk}%"
        )

    with col2:

        st.write("**Predicted Failure**")
        st.info(failure)

        st.write("**Recommendation**")
        st.success(recommendation)