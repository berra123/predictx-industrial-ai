import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

for _ in range(5000):

    current = np.random.normal(350, 40)
    temperature = np.random.normal(75, 10)
    vibration = np.random.normal(2.5, 1)
    torque = np.random.normal(650, 60)
    speed = np.random.normal(1450, 40)

    failure = 0

    if (
        temperature > 90 or
        vibration > 4.5 or
        current > 420
    ):
        failure = 1

    rows.append([
        current,
        temperature,
        vibration,
        torque,
        speed,
        failure
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "current",
        "temperature",
        "vibration",
        "torque",
        "speed",
        "failure"
    ]
)

df.to_csv(
    "data/training_data.csv",
    index=False
)

print("Training dataset created.")