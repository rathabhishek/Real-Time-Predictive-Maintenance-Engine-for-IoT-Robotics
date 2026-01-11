import tflite_runtime.interpreter as tflite
import numpy as np

# Load the TFLite model (optimized for IoT gateways)
interpreter = tflite.Interpreter(model_path="model_quantized.tflite")
interpreter.allocate_tensors()

def predict_on_edge(sensor_payload):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Inference logic for local Ubuntu-based Edge Compute [cite: 26]
    interpreter.set_tensor(input_details[0]['index'], sensor_payload)
    interpreter.invoke()
    
    prediction = interpreter.get_tensor(output_details[0]['index'])
    return prediction