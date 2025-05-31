# 🌡️📡 IoT Dashboard – Temperature & Light Monitoring

An interactive IoT dashboard built with **Streamlit**, **MQTT**, **SQLite**, and **Arduino**, designed to monitor and visualize **real-time temperature and light data**.

---

## 🚀 Features

- 📡 **Real-time data streaming** from Arduino via MQTT
- 📅 **Date range filtering** from the sidebar
- ⚠️ **Custom threshold alerts** (define your own temperature/light limits)
- 📉 **Separate line charts** for temperature and light
- 📈 **Statistics view**: Min, Max, and Average values
- 📥 **CSV export** of historical sensor data
- 🔄 **Auto-refresh**: Live dashboard updates every X seconds (customizable)

---

## 💡 Use Cases

- 🏠 Smart home / automation prototypes  
- 🌿 Smart farming / greenhouse monitoring  
- 🏫 Classroom or educational IoT demos  
- 📊 Real-time environmental monitoring  

---

## 🛠️ Tech Stack

- **Arduino** + LM35 (temperature sensor) + CDS (photoresistor)
- **Python** for serial reading and MQTT publishing
- **SQLite** to store sensor data locally
- **Streamlit** to build the interactive dashboard
- **MQTT** broker: [`test.mosquitto.org`](https://test.mosquitto.org) (public)

---

## ⚙️ Setup Instructions

### 1. Arduino

Upload the Arduino code from `arduino_code.ino`. Make sure your port matches the one used in the Python script (`COM3`, `COM4`, etc.).

### 2. Python Dependencies

Install required packages:

```bash
pip install -r requirements.txt





