import streamlit as st


def show_executive_insights(predictions):

    if not predictions:
        return

    latest = predictions[-1]

    risk = latest["ai_risk"]

    st.subheader("🧠 Executive Insights")

    if risk < 30:

        st.success("✔ Factory operating normally.")

        st.success("✔ No critical maintenance required.")

        st.success("✔ Production continues safely.")

    elif risk < 60:

        st.warning("⚠ Bearing wear probability increasing.")

        st.warning("⚠ Schedule maintenance planning.")

    else:

        st.error("🚨 Critical machine condition detected.")

        st.error("🚨 Immediate maintenance recommended.")