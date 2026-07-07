from services.anomaly_detector import detect_anomaly
from services.prediction_engine import make_prediction
from services.alarm_engine import create_alarm

from database.prediction_repository import insert_prediction


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

    # Anomali tespiti
    alarm = detect_anomaly(data)

    # Alarmı işle ve veritabanına kaydet
    create_alarm(
        data["machine"],
        alarm
    )

    return {
        "prediction": prediction,
        "alarm": alarm
    }