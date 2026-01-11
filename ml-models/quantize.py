import tensorflow as tf

# Convert LSTM to TFLite for Edge Devices
def optimize_for_edge(keras_model_path):
    model = tf.keras.models.load_model(keras_model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Apply quantization to reduce size for IoT hardware
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()

    with open('services/edge-gateway/model.tflite', 'wb') as f:
        f.write(tflite_model)
    print("✅ Optimized for Ubuntu Edge Compute")