import streamlit as st

from services.component_health_engine import (
    get_component_health
)


def get_color(health):

    if health >= 80:
        return "#2E7D32"

    elif health >= 60:
        return "#F9A825"

    return "#C62828"


def machine_box(title, health):

    color = get_color(health)

    st.markdown(
        f"""
<div style="
background:{color};
padding:18px;
border-radius:14px;
text-align:center;
font-weight:bold;
font-size:19px;
color:white;
margin-bottom:10px;
box-shadow:0px 4px 12px rgba(0,0,0,0.35);
">

{title}<br>
{health:.0f}%

</div>
""",
        unsafe_allow_html=True
    )


def arrow():

    st.markdown(
        """
<div style="
text-align:center;
font-size:30px;
font-weight:bold;
margin-bottom:8px;
">
⬇
</div>
""",
        unsafe_allow_html=True
    )


def show_pulper_twin(prediction):

    st.subheader("🏭 Pulper Digital Twin")

    components = get_component_health(
        prediction
    )

    machine_box(
        "⚙️ Motor",
        components["motor"]
    )

    arrow()

    machine_box(
        "⚙️ Gearbox",
        components["gearbox"]
    )

    arrow()

    machine_box(
        "🔩 Bearing",
        components["bearing"]
    )

    arrow()

    machine_box(
        "🛢️ Pulper Drum",
        components["drum"]
    )