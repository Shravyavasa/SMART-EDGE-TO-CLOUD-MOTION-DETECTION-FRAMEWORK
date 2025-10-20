import cv2
import numpy as np
import tensorflow as tf
import psutil
import requests
import time

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="mobilenet.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return cv2.resize(frame, (224, 224)) if ret else None

def run_local_inference(image):
    input_data = np.expand_dims(image, axis=0).astype(np.float32) / 255.0
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    return interpreter.get_tensor(output_details[0]['index'])

def should_offload():
    return psutil.cpu_percent() > 60 or psutil.virtual_memory().percent > 70

def send_to_cloud(image):
    _, img_encoded = cv2.imencode('.jpg', image)
    response = requests.post("http://<LAPTOP_IP>:5000/cloud_infer", files={"image": img_encoded.tobytes()})
    return response.json()

def handle_motion_trigger():
    image = capture_image()
    if image is None:
        return "Failed to capture"
    if should_offload():
        result = send_to_cloud(image)
        print("Offloaded result:", result)
    else:
        result = run_local_inference(image)
        print("Local result:", result.tolist())