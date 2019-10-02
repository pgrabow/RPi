# File:      getWeatherTemp.py
# Descr:     Get temp and id for a given city
# Created:   1 Oct 19
# Author:    P. Grabow

import requests
from pprint import pprint

# ------------ Convert Kelvin to Celcius
def kelvin_to_C(degreesK):
    return degreesK - 273.15

# ------------ Your API_KEY goes here 
OWM_API_KEY = '9bd0a4f6393cb71b355b2097f93753ca'

# ------------ The base address for OpenWeatherMap
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# ------------ What city? 
city_name = input("Enter a city Name : ")

# ------------ Append API_KEY and city_name to base address
Final_url = base_url + "appid=" + OWM_API_KEY + "&q=" + city_name
 
# ------------ Get the raw weather data
raw_data = requests.get(Final_url)

# ------------ Convert data to JSON
weather_data = raw_data.json()

# ------------ Print results
print('id: ', weather_data['id'])

temperature = weather_data['main']['temp']
print('current temp: ', kelvin_to_C(temperature))
