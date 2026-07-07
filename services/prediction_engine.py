def make_prediction(data):
    """
    AI Prediction Engine
    Telemetry verilerinden makine sağlığını analiz eder.
    """

    current = data["current"]
    temperature = data["temperature"]
    vibration = data["vibration"]
    torque = data["torque"]

    # ==========================
    # Health Score
    # ==========================

    health = 100

    # Current
    if current > 130:
        health -= 20
    elif current > 120:
        health -= 10

    # Temperature
    if temperature > 70:
        health -= 30
    elif temperature > 60:
        health -= 15

    # Vibration
    if vibration > 4:
        health -= 30
    elif vibration > 3:
        health -= 15

    # Torque
    if torque > 430:
        health -= 20
    elif torque > 400:
        health -= 10

    health = max(0, health)

    # ==========================
    # Risk
    # ==========================

    risk = 100 - health

    # Confidence
    confidence = max(80, 98 - risk // 4)

    # Remaining Useful Life
    remaining_life = max(5, 180 - (risk * 2))

    # ==========================
    # Failure Type
    # ==========================

    if risk < 30:

        failure = "Healthy"

        recommendation = "Continue Operation"

        diagnosis = {
            "Bearing Wear": 8,
            "Motor Failure": 2,
            "Overheating": 4,
            "Gearbox Wear": 6
        }

        maintenance = {
            "priority": "LOW",
            "action": "Routine Inspection",
            "duration": "1 Hour",
            "estimated_cost": "₺1.500",
            "next_inspection": "30 Days"
        }

    elif risk < 60:

        failure = "Bearing Wear"

        recommendation = "Schedule Inspection"

        diagnosis = {
            "Bearing Wear": 65,
            "Motor Failure": 12,
            "Overheating": 10,
            "Gearbox Wear": 13
        }

        maintenance = {
            "priority": "MEDIUM",
            "action": "Inspect Bearing",
            "duration": "2 Hours",
            "estimated_cost": "₺4.500",
            "next_inspection": "14 Days"
        }

    elif risk < 80:

        failure = "Mechanical Degradation"

        recommendation = "Maintenance Required"

        diagnosis = {
            "Bearing Wear": 82,
            "Motor Failure": 22,
            "Overheating": 30,
            "Gearbox Wear": 18
        }

        maintenance = {
            "priority": "HIGH",
            "action": "Replace Bearing",
            "duration": "4 Hours",
            "estimated_cost": "₺8.500",
            "next_inspection": "7 Days"
        }

    else:

        failure = "Critical Failure"

        recommendation = "Stop Machine Immediately"

        diagnosis = {
            "Bearing Wear": 94,
            "Motor Failure": 72,
            "Overheating": 86,
            "Gearbox Wear": 48
        }

        maintenance = {
            "priority": "CRITICAL",
            "action": "Immediate Shutdown & Maintenance",
            "duration": "6 Hours",
            "estimated_cost": "₺15.000",
            "next_inspection": "Today"
        }

    return {

        "health": health,

        "risk": risk,

        "failure": failure,

        "remaining_life": remaining_life,

        "confidence": confidence,

        "recommendation": recommendation,

        "diagnosis": diagnosis,

        "maintenance": maintenance
    }