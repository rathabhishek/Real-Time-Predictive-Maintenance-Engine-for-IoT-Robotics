from fastapi import FastAPI
import tensorflow as tf
import numpy as np

app = FastAPI(title="AegisML Inference API")
model = tf.keras.models.load_model("models/lstm_v1.h5")

@app.post("/predict")
async def predict(features: list):
    # features shape: (1, 50, 3) -> 1 batch, 50 timestamps, 3 sensors
    input_data = np.array(features).astype(np.float32)
    prediction = model.predict(input_data)
    
    # 0 = Healthy, 1 = Predicted Failure
    is_failure = bool(prediction[0][0] > 0.85)
    
    return {
        "failure_risk": float(prediction[0][0]),
        "alert": is_failure,
        "action": "SCHEDULE_MAINTENANCE" if is_failure else "NONE"
    }

@app.get("/health")
def health():
    return {"status": "99.99% Uptime Active"}