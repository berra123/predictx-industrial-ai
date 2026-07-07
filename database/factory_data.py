from services.ai_engine import process_telemetry

from database.telemetry_repository import insert_telemetry

from data_sources.demo_source import get_demo_data
from data_sources.history_buffer import add_record

MODE = "DEMO"
# MODE = "PRODUCTION"


def get_factory_data():

    if MODE == "DEMO":

        data = get_demo_data()

        # History Buffer
        add_record(data)

        # MySQL
        insert_telemetry(data)

        # AI
        ai_result = process_telemetry(data)

        return {
            "telemetry": data,
            "prediction": ai_result["prediction"],
            "alarm": ai_result["alarm"]
        }

    elif MODE == "PRODUCTION":

        return {}

    return {}