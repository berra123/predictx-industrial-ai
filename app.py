import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Tema
from utils.theme import apply_theme

# Sidebar
from components.sidebar import render_sidebar

# Sayfalar
from app_pages.dashboard import show_dashboard
from app_pages.pulper import show_pulper
from app_pages.alarms import show_alarms
from app_pages.reports import show_reports
from app_pages.settings import show_settings


# Tema
apply_theme()

# Otomatik yenileme (2 saniye)
st_autorefresh(
    interval=2000,
    key="predictx_refresh"
)

# Sidebar
selected_page = render_sidebar()

# Sayfa Yönlendirme
if selected_page == "🏠 Dashboard":
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
    st.error("Sayfa bulunamadı.")