import requests
import random
import time

PLANT_ID = 1
API_URL = f"http://127.0.0.1:8000/plants/{PLANT_ID}/readings/"

def generate_reading():
    return {
        "temperature": round(random.uniform(10, 40), 1),
        "humidity": round(random.uniform(20, 90), 1),
        "light_level": round(random.uniform(100, 1000), 1)
    }

print("🌱 Simulating sensor data... Press Ctrl+C to stop")

while True:
    data = generate_reading()
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"✅ Sent: {data}")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Could not reach API: {e}")
    
    time.sleep(5)  # sends a new reading every 5 seconds