import tensorflow as tf

def convert_to_tflite(model_path):
    # Load the trained LSTM model
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Apply post-training quantization to reduce size for IoT devices
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()

    with open('services/edge-gateway/model_quantized.tflite', 'wb') as f:
        f.write(tflite_model)
    print("✅ Model optimized for Edge Compute")

if __name__ == "__main__":
    convert_to_tflite('ml-models/lstm_v1.h5')