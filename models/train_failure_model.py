import pandas as pd
import joblib

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Dataset
df = pd.read_csv("data/training_data.csv")

# Features
X = df[
    [
        "current",
        "temperature",
        "vibration",
        "torque",
        "speed"
    ]
]

# Target
y = df["failure"]

# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

# Training
model.fit(
    X_train,
    y_train
)

# Prediction
predictions = model.predict(X_test)

# Metrics
accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nAccuracy: {accuracy:.4f}\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

# Save model
joblib.dump(
    model,
    "models/failure_model.pkl"
)

print("\nModel saved successfully.")