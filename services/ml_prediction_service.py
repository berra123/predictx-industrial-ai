import joblib
import pandas as pd

model = joblib.load(
    "models/failure_model.pkl"
)


def predict_failure(
    current,
    temperature,
    vibration,
    torque,
    speed
):

    data = pd.DataFrame(
        [[
            current,
            temperature,
            vibration,
            torque,
            speed
        ]],
        columns=[
            "current",
            "temperature",
            "vibration",
            "torque",
            "speed"
        ]
    )

    prediction = model.predict(data)[0]

    probability = model.predict_proba(
        data
    )[0][1]

    return prediction, probability