import joblib
import pandas as pd

model = joblib.load(
    "ml/models/risk_model.pkl"
)


def predict_risk(
    current,
    temperature,
    vibration,
    torque
):

    data = pd.DataFrame(
        [[
            current,
            temperature,
            vibration,
            torque
        ]],
        columns=[
            "current",
            "temperature",
            "vibration",
            "torque"
        ]
    )

    risk = model.predict(data)[0]

    return round(
        risk,
        1
    )