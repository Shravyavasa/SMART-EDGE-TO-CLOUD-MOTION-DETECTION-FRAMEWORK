import paho.mqtt.client as mqtt
import subprocess

MQTT_BROKER = "localhost"
MQTT_TOPIC = "motion/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print("Motion detected! Capturing image...")
    subprocess.run(["python3", "capture_and_process.py"])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_forever()