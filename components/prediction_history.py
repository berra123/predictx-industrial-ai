import streamlit as st

from database.prediction_read_repository import (
    get_last_100_predictions
)


def show_prediction_history():

    st.subheader("🤖 Prediction History")

    predictions = get_last_100_predictions()

    if not predictions:
        st.info("No prediction history available.")
        return

    for prediction in reversed(predictions[-10:]):

        risk = prediction["ai_risk"]

        if risk >= 80:
            color = "#C62828"
            icon = "🔴"

        elif risk >= 50:
            color = "#F9A825"
            icon = "🟡"

        else:
            color = "#2E7D32"
            icon = "🟢"

        st.markdown(
            f"""
<div style="
border-left:6px solid {color};
padding:10px;
margin-bottom:10px;
background:#1B1E23;
border-radius:8px;
">

<b>{icon} {prediction['predicted_failure']}</b><br>

Risk Score: {prediction['ai_risk']}%<br>

Remaining Life: {prediction['remaining_life']} Days<br>

Confidence: {prediction['confidence']}%<br>

<small>{prediction['timestamp']}</small>

</div>
""",
            unsafe_allow_html=True
        )