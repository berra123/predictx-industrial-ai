import streamlit as st
import pandas as pd

from database.work_order_repository import get_work_orders


def show_work_orders():

    st.title("🛠 SAP PM Work Orders")
    st.caption(
        "Automatically generated maintenance orders"
    )

    orders = get_work_orders()

    if len(orders) == 0:
        st.info(
            "No work orders available."
        )
        return

    df = pd.DataFrame(orders)

    st.metric(
        "Open Work Orders",
        len(
            df[df["status"] == "OPEN"]
        )
    )

    st.divider()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )