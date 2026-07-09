from services.anomaly_detector import detect_anomaly
from services.prediction_engine import make_prediction
from services.alarm_engine import create_alarm
from services.event_engine import log_event
from services.email_service import send_email_notification

from database.prediction_repository import insert_prediction
from database.settings_repository import get_setting


def process_telemetry(data):
    """
    Yeni telemetri verisini işler.
    """

    # AI tahmini oluştur
    prediction = make_prediction(data)

    # Tahmini veritabanına kaydet
    insert_prediction(
        data["machine"],
        prediction
    )

    # AI Prediction Event
    log_event(
        "PREDICTION",
        "AI Prediction Generated",
        f"Risk Score: {prediction['risk']}%"
    )

    # Anomali tespiti
    alarm = detect_anomaly(data)

    # Alarmı işle ve veritabanına kaydet
    create_alarm(
        data["machine"],
        alarm
    )

    # Alarm Event
    if alarm["level"] != "NORMAL":

        log_event(
            "ALARM",
            f"{alarm['level']} Alarm",
            alarm.get("description", "No description")
        )

        # Email Notification
        email_enabled = (
            get_setting(
                "email_notifications",
                "False"
            ) == "True"
        )

        if (
            email_enabled and
            alarm["level"] in ["HIGH", "CRITICAL"]
        ):

            send_email_notification(
                data["machine"],
                alarm
            )

            log_event(
                "EMAIL",
                "Notification Sent",
                f"{alarm['level']} email sent for {data['machine']}"
            )

    return {
        "prediction": prediction,
        "alarm": alarm
    }