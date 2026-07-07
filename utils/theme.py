import streamlit as st


PRIMARY = "#2563EB"
SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"
BACKGROUND = "#0F172A"
CARD = "#1E293B"
TEXT = "#F8FAFC"
SECONDARY = "#94A3B8"


def apply_theme():
    st.set_page_config(
        page_title="PredictX Industrial AI",
        page_icon="🏭",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-color: {BACKGROUND};
            color:{TEXT};
        }}

        section[data-testid="stSidebar"] {{
            background-color:#111827;
        }}

        h1,h2,h3,h4,h5,h6,p,label,span {{
            color:{TEXT};
        }}

        div[data-testid="metric-container"] {{
            background-color:{CARD};
            padding:20px;
            border-radius:15px;
            border:1px solid #334155;
        }}

        div[data-testid="metric-container"] label {{
            color:{SECONDARY};
        }}

        div[data-testid="metric-container"] div {{
            color:white;
        }}

        .block-container {{
            padding-top:1rem;
            padding-bottom:1rem;
            padding-left:2rem;
            padding-right:2rem;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )