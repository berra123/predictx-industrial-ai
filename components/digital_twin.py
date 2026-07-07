import streamlit as st


def show_digital_twin():

    st.subheader("🏭 Production Line Digital Twin")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.success("🟢 Pulper")
        st.caption("Running")

    with col2:
        st.success("🟢 Cleaner")
        st.caption("Running")

    with col3:
        st.success("🟢 Paper Machine")
        st.caption("Running")

    with col4:
        st.warning("🟡 Corrugator")
        st.caption("Waiting")

    with col5:
        st.success("🟢 Printing")
        st.caption("Running")

    with col6:
        st.success("🟢 Finishing")
        st.caption("Running")