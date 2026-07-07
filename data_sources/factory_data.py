from services.ai_engine import process_telemetry

from database.telemetry_repository import insert_telemetry

from data_sources.demo_source import get_demo_data
from data_sources.history_buffer import add_record

MODE = "DEMO"
# MODE = "PRODUCTION"


def get_factory_data():

    if MODE == "DEMO":

        data = get_demo_data()

        add_record(data)

        insert_telemetry(data)

        ai_result = process_telemetry(data)

        return {
            "telemetry": data,
            "prediction": ai_result["prediction"],
            "alarm": ai_result["alarm"]
        }

    elif MODE == "PRODUCTION":

        # Gelecekte OPC-UA buraya gelecek
        return {}

    return {}