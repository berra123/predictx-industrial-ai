import random
import pandas as pd


rows = []

for _ in range(5000):

    current = random.uniform(100, 145)
    temperature = random.uniform(50, 80)
    vibration = random.uniform(1.5, 5.5)
    torque = random.uniform(380, 450)

    risk = 0

    if current > 130:
        risk += 20
    elif current > 120:
        risk += 10

    if temperature > 70:
        risk += 30
    elif temperature > 60:
        risk += 15

    if vibration > 4:
        risk += 30
    elif vibration > 3:
        risk += 15

    if torque > 430:
        risk += 20
    elif torque > 400:
        risk += 10

    risk = min(risk, 100)

    rows.append({
        "current": current,
        "temperature": temperature,
        "vibration": vibration,
        "torque": torque,
        "risk": risk
    })


df = pd.DataFrame(rows)

df.to_csv(
    "ml/dataset.csv",
    index=False
)

print("Dataset generated successfully.")
print(df.head())