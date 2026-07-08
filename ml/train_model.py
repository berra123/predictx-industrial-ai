import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# Dataset
df = pd.read_csv("ml/dataset.csv")

# Features
X = df[
    [
        "current",
        "temperature",
        "vibration",
        "torque"
    ]
]

# Target
y = df["risk"]

# Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Training
model.fit(
    X_train,
    y_train
)

# Prediction
predictions = model.predict(X_test)

# Metric
mae = mean_absolute_error(
    y_test,
    predictions
)

print(
    f"MAE: {mae:.2f}"
)

# Save Model
joblib.dump(
    model,
    "ml/models/risk_model.pkl"
)

print(
    "Model saved successfully."
)