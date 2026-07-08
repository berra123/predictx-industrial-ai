import streamlit as st


def show_plc_info():

    st.subheader("🏭 Machine Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Machine ID",
            "Pulper-03"
        )

        st.metric(
            "PLC",
            "Siemens S7-1200"
        )

        st.metric(
            "Protocol",
            "OPC-UA"
        )

        st.metric(
            "Location",
            "Production Line A"
        )

    with col2:

        st.metric(
            "Motor Power",
            "250 kW"
        )

        st.metric(
            "Voltage",
            "400 V"
        )

        st.metric(
            "Drive",
            "ABB ACS580"
        )

        st.metric(
            "Status",
            "ONLINE"
        )