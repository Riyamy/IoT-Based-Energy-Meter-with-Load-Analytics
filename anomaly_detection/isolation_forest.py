import paho.mqtt.client as mqtt
import json
import pandas as pd
from sklearn.ensemble import IsolationForest

BROKER = "localhost"
PORT = 1883
TOPIC = "energy/data"

model = IsolationForest(contamination=0.05, random_state=42)
data_buffer = []

def on_message(client, userdata, msg):
    global data_buffer
    payload = json.loads(msg.payload.decode())
    data_buffer.append(payload["energy_usage"])

    if len(data_buffer) > 50:
        df = pd.DataFrame(data_buffer, columns=["energy_usage"])
        preds = model.fit_predict(df)
        latest = preds[-1]

        if latest == -1:
            print(f"⚠️ Anomaly Detected: {payload}")
        else:
            print(f"✅ Normal: {payload}")

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.on_message = on_message

print("🚨 Anomaly Detection Running...")
client.loop_forever()
