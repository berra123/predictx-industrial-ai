import streamlit as st


def component_color(component, prediction):

    risk = prediction["risk"]
    failure = prediction["failure"]

    # Varsayılan renk
    color = "#2E7D32"

    if risk >= 70:

        if "Bearing" in failure and component == "Bearing":
            color = "#C62828"

        elif "Motor" in failure and component == "Motor":
            color = "#C62828"

        elif "Temperature" in failure and component == "Motor":
            color = "#EF6C00"

        else:
            color = "#F9A825"

    elif risk >= 40:
        color = "#F9A825"

    return color


def machine_box(title, color):

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

{title}

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

    machine_box(
        "⚙️ Motor",
        component_color("Motor", prediction)
    )

    arrow()

    machine_box(
        "⚙️ Gearbox",
        component_color("Gearbox", prediction)
    )

    arrow()

    machine_box(
        "🔩 Bearing",
        component_color("Bearing", prediction)
    )

    arrow()

    machine_box(
        "🛢️ Pulper Drum",
        component_color("Drum", prediction)
    )