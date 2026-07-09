import streamlit as st

from utils.theme import apply_theme

from components.sidebar import render_sidebar

from app_pages.dashboard import show_dashboard
from app_pages.pulper import show_pulper
from app_pages.alarms import show_alarms
from app_pages.reports import show_reports
from app_pages.settings import show_settings
from app_pages.work_orders import show_work_orders


apply_theme()

selected_page = render_sidebar()


if selected_page == "📈 Dashboard":
    show_dashboard()

elif selected_page == "🏭 Pulper":
    show_pulper()

elif selected_page == "🚨 Alarm Center":
    show_alarms()

elif selected_page == "🛠 Work Orders":
    show_work_orders()

elif selected_page == "📊 Reports":
    show_reports()

elif selected_page == "⚙️ Settings":
    show_settings()

else:
    st.error("Page not found.")