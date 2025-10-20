from flask import Flask
from main import handle_motion_trigger

app = Flask(__name__)

@app.route('/motion_trigger', methods=['POST'])
def motion_trigger():
    handle_motion_trigger()
    return "Triggered", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)