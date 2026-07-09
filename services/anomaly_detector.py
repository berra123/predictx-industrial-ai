def detect_anomaly(data):

    if (
        data["temperature"] > 85
        or data["vibration"] > 5
        or data["current"] > 150
    ):
        return {
            "level": "CRITICAL",
            "type": "Motor Failure",
            "description": "Immediate shutdown recommended."
        }

    elif (
        data["temperature"] > 70
        or data["vibration"] > 4
        or data["current"] > 135
    ):
        return {
            "level": "HIGH",
            "type": "Overheating",
            "description": "Maintenance should be scheduled immediately."
        }

    elif (
        data["temperature"] > 60
        or data["vibration"] > 3
        or data["current"] > 120
    ):
        return {
            "level": "MEDIUM",
            "type": "Bearing Wear",
            "description": "Check machine parameters."
        }

    return {
        "level": "NORMAL",
        "type": "No Alarm",
        "description": "Machine operating normally."
    }