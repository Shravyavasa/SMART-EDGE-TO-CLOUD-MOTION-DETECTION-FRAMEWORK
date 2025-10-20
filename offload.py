import requests

CLOUD_INFERENCE_URL = "https://your-cloud.com/inference"

def offload_to_cloud(image_path):
    print("Offloading to cloud...")
    with open(image_path, 'rb') as img:
        files = {'image': img}
        try:
            res = requests.post(CLOUD_INFERENCE_URL, files=files)
            result = res.json()
            print(f"Cloud Inference: {result}")
        except Exception as e:
            print("Failed to offload:", e)