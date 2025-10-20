from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import io

app = Flask(__name__)
interpreter = tf.lite.Interpreter(model_path="heavy_model.tflite")
interpreter.allocate_tensors()

@app.route('/inference', methods=['POST'])
def inference():
    file = request.files['image']
    img_arr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224)).astype(np.float32)
    img = np.expand_dims(img, axis=0)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])

    return jsonify({"result": output.tolist()})

@app.route('/ping')
def ping():
    return "pong", 200

app.run()