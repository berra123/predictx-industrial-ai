def detect_anomaly(data):
    """
    Telemetri verisini analiz ederek alarm seviyesini belirler.
    """

    if (
        data["temperature"] > 70
        or data["vibration"] > 4
        or data["current"] > 135
    ):
        return {
            "level": "HIGH",
            "type": "Critical Condition",
            "description": "Immediate maintenance required."
        }

    elif (
        data["temperature"] > 60
        or data["vibration"] > 3
        or data["current"] > 120
    ):
        return {
            "level": "MEDIUM",
            "type": "Warning",
            "description": "Check machine parameters."
        }

    return {
        "level": "NORMAL",
        "type": "No Alarm",
        "description": "Machine operating normally."
    }