from flask import Flask, request, jsonify
import numpy as np
import cv2
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model("cloud_model.h5")  # Use a full model

@app.route('/cloud_infer', methods=['POST'])
def cloud_infer():
    img_file = request.files['image']
    img_np = np.frombuffer(img_file.read(), np.uint8)
    image = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224)).astype(np.float32) / 255.0
    pred = model.predict(np.expand_dims(image, axis=0))
    return jsonify(pred.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)