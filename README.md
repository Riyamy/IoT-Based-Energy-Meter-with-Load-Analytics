# ⚡ IoT-Based Energy Meter with Load Analytics

This project simulates an **IoT-based smart energy monitoring system** that enables **real-time energy usage tracking, anomaly detection, and load analytics**.  
It integrates IoT data streams, a machine learning anomaly detection model, and a visualization dashboard for end-to-end energy insights.

---

## 🎯 Objectives
- Develop a simulated IoT-based energy monitoring system with real-time data analytics.  
- Generate synthetic IoT sensor data via MQTT protocol.  
- Detect abnormal energy consumption patterns using **Isolation Forest (ML)**.  
- Provide a real-time **Grafana dashboard** for load insights.  
- Demonstrate **end-to-end IoT pipeline integration**.

---

## 🛠️ Tech Stack
- **IoT Simulation:** Python, MQTT (paho-mqtt)  
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **Data Pipeline:** MQTT Broker (Eclipse Mosquitto), Python Processor  
- **Visualization:** Grafana  
- **Environment:** Docker / Localhost  

---

## 📊 Features
- ✅ Synthetic IoT energy consumption data generation  
- ✅ Real-time MQTT streaming  
- ✅ Isolation Forest–based anomaly detection  
- ✅ Data processing & storage pipeline  
- ✅ Grafana dashboard for monitoring and insights  
- ✅ Demonstrated **10% simulated energy savings** by identifying high-consumption loads  

---

## ⚙️ Setup & Run

### 1. Clone Repository
```bash
git clone https://github.com/your-username/IoT-Based-Energy-Meter-with-Load-Analytics.git
cd IoT-Based-Energy-Meter-with-Load-Analytics
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start MQTT Broker & Grafana (Docker)
```bash
docker-compose up -d
```

### 4. Run IoT Data Generator
```bash
python mqtt_simulator/data_generator.py
```

### 5. Start Anomaly Detection
```bash
python anomaly_detection/isolation_forest.py
```

### 6. Start Data Processor
```bash
python pipeline/processor.py
```

### 7. Open Grafana Dashboard
- URL: [http://localhost:3000](http://localhost:3000)  
- Login: `admin / admin`  

---



## 📈 Outcomes
- Built a simulated IoT energy monitoring platform with **scalable data streaming**.  
- Implemented **Isolation Forest anomaly detection** with high accuracy.  
- Delivered a **real-time Grafana dashboard** for monitoring and analytics.  
- Showcased strong skills in **IoT pipelines, ML integration, and visualization**.  

---


