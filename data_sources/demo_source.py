from datetime import datetime

from models.scenario_engine import scenario


def get_demo_data():
    """
    Demo senaryosundan bir sonraki telemetri verisini alır.
    """

    data = scenario.next()

    return {

        "timestamp": datetime.now(),

        "machine": "Pulper-03",

        "status": "Running",

        "current": data["current"],

        "temperature": data["temperature"],

        "vibration": data["vibration"],

        "torque": data["torque"],

        "speed": 1475

    }