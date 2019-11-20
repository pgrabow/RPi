# File:     dht22_hass.py
# Created:  11/20/2019
# By:       P. Grabow
# Descr:    Modification of dht22-mqtt.py
from time import sleep
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import struct

# Address of Home Assistant (subsitute your IP address)
HOST = '192.168.50.64'
PORT = 1883

# Hardware location
DHT_SENSOR = Adafruit_DHT.DHT22
GPIO_PIN = 23

# create client object
client = mqtt.Client()                       
connect_flag = 0

while True :
    # Read values from DHT22
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, GPIO_PIN)
    
    # Print values to terminal window
    print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))

    # Connect to MQTT host/port
    connect_flag = client.connect(HOST, PORT, 60)
    if(connect_flag != 0):
        print("Error: connect", connect_flag)
        
    # Publish values to MQTT host/port
    client.publish('home/indoor/temperature', round(temperature), 1) 
    client.publish('home/indoor/humidity', round(humidity), 1)
    
    # Sleep for 60 seconds
    sleep(60)
        

client.disconnect()
sleep(10)
