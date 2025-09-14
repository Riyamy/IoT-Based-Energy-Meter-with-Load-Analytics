import time, random, json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "energy/data"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("🔌 IoT Energy Data Generator Started...")

while True:
    energy_usage = random.uniform(50, 500)
    message = {"device_id": "meter-01","timestamp": time.time(),"energy_usage": round(energy_usage, 2)}
    client.publish(TOPIC, json.dumps(message))
    print(f"Published: {message}")
    time.sleep(2)
