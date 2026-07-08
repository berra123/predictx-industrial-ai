import streamlit as st

# Tema
from utils.theme import apply_theme

# Sidebar
from components.sidebar import render_sidebar

# Sayfalar
from app_pages.executive import show_executive
from app_pages.dashboard import show_dashboard
from app_pages.pulper import show_pulper
from app_pages.alarms import show_alarms
from app_pages.reports import show_reports
from app_pages.settings import show_settings


apply_theme()

selected_page = render_sidebar()

if selected_page == "📈 Executive Dashboard":
    show_executive()

elif selected_page == "🏠 Dashboard":
    show_dashboard()

elif selected_page == "🏭 Pulper":
    show_pulper()

elif selected_page == "🚨 Alarm Center":
    show_alarms()

elif selected_page == "📊 Reports":
    show_reports()

elif selected_page == "⚙️ Settings":
    show_settings()

else:
    st.error("Page not found.")