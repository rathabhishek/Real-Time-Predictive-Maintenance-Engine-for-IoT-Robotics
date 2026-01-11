import tensorflow as tf

# Convert the trained LSTM model to TFLite format for Edge Devices
def convert_to_edge_model(model_path):
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Apply quantization to reduce size by 4x for IoT Gateways
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()

    with open('services/edge-gateway/model_quantized.tflite', 'wb') as f:
        f.write(tflite_model)
    print("✅ Model optimized for Edge Deployment.")

if __name__ == "__main__":
    convert_to_edge_model('models/lstm_v1.h5')