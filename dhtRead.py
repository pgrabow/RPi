"""
File:     dhtRead.py
Ref:      from https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
Modified: 10/4/2019
By:       P. Grabow
To:       change GPIO04 to GPIO23; changed DHT_PIN to GPIO_PIN
"""

import Adafruit_DHT
from time import sleep

DHT_SENSOR = Adafruit_DHT.DHT22
GPIO_PIN = 23

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, GPIO_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        sleep(30)
    else:
        print("Failed to retrieve data from humidity sensor")