from services.work_order_service import create_work_order
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

    # Alarmı veritabanına kaydet
    create_alarm(
        data["machine"],
        alarm
    )

    # Alarm oluştuysa
    if alarm["level"] != "NORMAL":

        # Alarm Event
        log_event(
            "ALARM",
            f"{alarm['level']} Alarm",
            alarm.get(
                "description",
                "No description"
            )
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

        # SAP PM Work Order Simulation
        if alarm["level"] in ["HIGH", "CRITICAL"]:

            work_order_no = create_work_order(
                data["machine"],
                alarm
            )

            log_event(
                "WORK_ORDER",
                "SAP PM Work Order Created",
                f"Maintenance Order Created: {work_order_no}"
            )

    return {
        "prediction": prediction,
        "alarm": alarm
    }