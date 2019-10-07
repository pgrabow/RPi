"""
File: WeatherData.py
Chap: 7
Date: 10/7/2019
"""
import requests
import time

class WeatherData:
    temperature = 0
    weather_conditions = ''
    wind_speed = 0
    city = ''
    
    OWM_API_KEY = '9bd0a4f6393cb71b355b2097f93753cf'
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
 
    def __init__(self,city):
        self.city = city
        Final_url = self.BASE_URL + "appid=" + self.OWM_API_KEY + "&q=" + city
        raw_data = requests.get(Final_url)
        weather_data = raw_data.json()
        tempK = weather_data['main']['temp']
        self.temperature = tempK - 273.15
        self.weather_conditions = weather_data['weather'][0]['main']
        self.wind_speed = weather_data['wind']['speed']
   
    def getCity(self):
        return self.city
    
    def getTemperature(self):
        return self.temperature
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed
    
    def getTime(self):
        return time.ctime()
    
def main():
    current_weather = WeatherData('Ulaanbaatar')
    print(current_weather.getTime())
    print(current_weather.getCity())
    print(str(current_weather.getTemperature()) + ' C')
    print(current_weather.getWeatherConditions())
    print(str(current_weather.getWindSpeed()) + ' mph')
        
if __name__ == "__main__":
    main()
    
""" sample output
Mon Oct  7 12:30:35 2019
Ulaanbaatar
-3.0 C
Clear
1 mph
"""