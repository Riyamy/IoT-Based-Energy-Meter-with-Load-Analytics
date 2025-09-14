import paho.mqtt.client as mqtt
import json
import pandas as pd

BROKER = "localhost"
PORT = 1883
TOPIC = "energy/data"

log_file = "energy_log.csv"
columns = ["device_id", "timestamp", "energy_usage"]

df = pd.DataFrame(columns=columns)
df.to_csv(log_file, index=False)

def on_message(client, userdata, msg):
    global df
    payload = json.loads(msg.payload.decode())
    print(f"📥 Processing: {payload}")

    new_row = pd.DataFrame([payload])
    new_row.to_csv(log_file, mode='a', header=False, index=False)

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.on_message = on_message

print("🔄 Data Processor Running...")
client.loop_forever()
