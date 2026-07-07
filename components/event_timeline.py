import streamlit as st

from database.event_read_repository import get_last_20_events


def show_event_timeline():

    st.subheader("🕒 Live Event Timeline")

    events = get_last_20_events()

    if not events:
        st.info("No events available.")
        return

    colors = {
        "PREDICTION": "#1E88E5",
        "ALARM": "#E53935",
        "SYSTEM": "#43A047",
        "DEMO": "#FB8C00"
    }

    icons = {
        "PREDICTION": "🤖",
        "ALARM": "🚨",
        "SYSTEM": "⚙️",
        "DEMO": "🎬"
    }

    for event in reversed(events):

        color = colors.get(event["event_type"], "#546E7A")
        icon = icons.get(event["event_type"], "📌")

        st.markdown(
            f"""
<div style="
border-left:6px solid {color};
padding:10px;
margin-bottom:10px;
background:#1B1E23;
border-radius:8px;
">

<b>{icon} {event['title']}</b><br>

<small>{event['timestamp']}</small>

<br><br>

{event['description']}

</div>
""",
            unsafe_allow_html=True
        )