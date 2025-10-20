from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/motion', methods=['POST'])
def motion_triggered():
    print("Motion detected! Capturing image...")
    subprocess.run(["python3", "capture_and_process.py"])
    return {"status": "received"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)