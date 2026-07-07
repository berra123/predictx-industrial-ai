import streamlit as st


def show_ai_diagnosis(prediction):

    st.subheader("🧠 AI Diagnosis")

    diagnosis = prediction["diagnosis"]

    for name, probability in diagnosis.items():

        st.write(f"**{name}**")

        st.progress(probability / 100)

        st.caption(f"{probability}% probability")