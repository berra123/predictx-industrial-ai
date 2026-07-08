from services.ml_prediction_service import predict_failure

prediction, probability = predict_failure(
    current=430,
    temperature=95,
    vibration=5.3,
    torque=760,
    speed=1420
)

print("Prediction:", prediction)
print("Risk:", probability)