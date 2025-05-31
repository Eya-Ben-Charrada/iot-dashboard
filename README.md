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
```
---
### 3. Start Serial to MQTT + Database Logger
Run the following command in your terminal:

```bash
python serial_to_mqtt.py
```
This script will:

- 📥 Read serial data from the Arduino  
- 📡 Publish the data to the MQTT broker (`test.mosquitto.org`)  
- 💾 Store readings in a local SQLite database (`sensor_data.db`)  

Make sure:

- ✅ Your Arduino is connected and sending serial data like `TEMP:25.42;LIGHT:73`  
- 🔧 You set the correct COM port in `serial_to_mqtt.py` (e.g., `'COM3'`, `'COM4'`, etc., depending on your system)

---
### 🌐 4. Launch the Streamlit Dashboard
Start the dashboard with:
```bash
streamlit run streamlit_app.py
```

From here you can:

- 📊 View real-time temperature and light charts  
- 📅 Filter by date range  
- ⚠️ Set custom threshold alerts  
- 📥 Download data as CSV  
- 🔄 See auto-refreshing data every X seconds




⚠️ **Important Notes**

- Make sure your Arduino is connected and sending serial data like:  
  `TEMP:25.42;LIGHT:73`

- Update the **COM port** in `serial_to_mqtt.py` to match your system (e.g., `'COM3'`, `'COM4'`, etc.)

- Adjust the **SQLite database path** in both `serial_to_mqtt.py` and `streamlit_app.py` to match your local environment.  
  Example path:  
  `C:/Users/YourUsername/Documents/serial_mqtt/sensor_data.db`

- The MQTT broker used (`test.mosquitto.org`) is public. For production, consider using a private or secure broker like HiveMQ or Mosquitto with TLS.

