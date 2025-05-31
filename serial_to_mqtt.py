import serial
import time
import paho.mqtt.client as mqtt

# MQTT Setup
broker = "test.mosquitto.org"
port = 1883
topic = "home/sensors/data"

client = mqtt.Client()
client.connect(broker, port, 60)

# Serial Setup
ser = serial.Serial('COM3', 9600, timeout=1)  # Change COM3 to your port
time.sleep(2)  # Wait for serial connection to initialize

print("Reading from Arduino and publishing to MQTT...")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print("Serial:", line)
            client.publish(topic, line)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")
    ser.close()
    client.disconnect()
