""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016
Ref: https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4
------------------
Modified: 10/3/2019
By:       P. Grabow
To:       Remove Thingspeak calls
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
#import urllib2 
#myAPI = "<your API code here>" 
def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23) 
   return (str(RH), str(T))

def main(): 
   print 'starting...' 
#   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
   while True: 
       try: 
           strTemp, temp = getSensorData()
           print("current temp: {TEMP:4.0f}".format(TEMP=temp))
#           f = urllib2.urlopen(baseURL + 
#                               "&field1=%s&field2=%s" % (RH, T)) 
#           print f.read() 
#           f.close() 
           sleep(300) #uploads DHT22 sensor values every 5 minutes 
       except: 
           print 'exiting.' 
           break 
# call main 
if __name__ == '__main__': 
   main() 