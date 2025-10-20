import numpy as np
import cv2
import tensorflow as tf

MODEL_PATH = "light_model.tflite"
LABELS = ["cat", "dog", "person"]  # Replace with your labels

def run_local_inference(image_path):
    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (224, 224))
    input_data = np.expand_dims(img_resized, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    predicted_label = LABELS[np.argmax(output_data)]
    confidence = np.max(output_data)
    print(f"Local Inference: {predicted_label} ({confidence:.2f})")