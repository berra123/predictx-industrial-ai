from services.ai_engine import process_telemetry

from database.telemetry_repository import insert_telemetry
from database.prediction_repository import insert_prediction
from database.alarm_repository import insert_alarm

from data_sources.demo_source import get_demo_data
from data_sources.history_buffer import add_record

MODE = "DEMO"
# MODE = "PRODUCTION"


def get_factory_data():

    if MODE == "DEMO":

        data = get_demo_data()

        # History Buffer
        add_record(data)

        # Telemetry -> PostgreSQL
        insert_telemetry(data)

        # AI
        ai_result = process_telemetry(data)

        # Prediction -> PostgreSQL
        insert_prediction(
            data["machine"],
            ai_result["prediction"]
        )
        # Alarm -> PostgreSQL
        insert_alarm(
            data["machine"],
            ai_result["alarm"]
        )

        return {
            "telemetry": data,
            "prediction": ai_result["prediction"],
            "alarm": ai_result["alarm"]
        }

    elif MODE == "PRODUCTION":

        return {}

    return {}