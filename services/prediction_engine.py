def make_prediction(data):
    """
    Makinenin risk skorunu hesaplar.
    """

    risk = 10

    if data["temperature"] > 60:
        risk += 25

    if data["vibration"] > 3:
        risk += 30

    if data["torque"] > 430:
        risk += 20

    if risk > 100:
        risk = 100

    if risk < 40:
        failure = "Healthy"
        remaining_life = 120
        recommendation = "Continue Operation"

    elif risk < 70:
        failure = "Maintenance Recommended"
        remaining_life = 60
        recommendation = "Inspect Bearings"

    else:
        failure = "High Failure Risk"
        remaining_life = 10
        recommendation = "Stop Machine"

    return {
        "risk": risk,
        "failure": failure,
        "remaining_life": remaining_life,
        "confidence": 95,
        "recommendation": recommendation
    }