import cv2
import time
import psutil
import requests
from inference import run_local_inference
from offload import offload_to_cloud

IMAGE_PATH = "latest.jpg"
CLOUD_PING_URL = "https://your-cloud.com/ping"

def capture_image():
    cam = cv2.VideoCapture(0)
    time.sleep(2)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(IMAGE_PATH, frame)
        print("Image captured.")
    cam.release()

def should_offload():
    cpu = psutil.cpu_percent()
    try:
        start = time.time()
        requests.get(CLOUD_PING_URL, timeout=1)
        latency = time.time() - start
    except:
        latency = float('inf')
    print(f"CPU: {cpu}%, Latency: {latency:.2f}s")
    return cpu > 70 and latency < 0.5

if __name__ == "__main__":
    capture_image()
    if should_offload():
        offload_to_cloud(IMAGE_PATH)
    else:
        run_local_inference(IMAGE_PATH)
        