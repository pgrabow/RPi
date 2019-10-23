"""
File: Dashboard3.py
From: https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_default&stacked=h
From: Modification of WeatherDashboardHtml.py from Chapter 7 of Dow
"""
import cherrypy
from WeatherData3 import WeatherData3

class Dashboard3:
    
    def __init__(self, weather):
        self.currentWeather = weather
    
    def getTemp(self):
        return format(self.currentWeather.getTemperature(), '.0f')
    
    def getConditions(self):
        return self.currentWeather.getWeatherConditions()
    
    def getWindspeed(self):
        return format(self.currentWeather.getWindSpeed(), '.0f')
    
    @cherrypy.expose
    def index(self):
        return """
              <!DOCTYPE html>
                <html lang="en">
                <head>
                <title>Bootstrap Example</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
                <script
                    src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                <script
                    src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
                </head>
                <body>

                    <div class="jumbotron text-center">
                        <h1>Weather Conditions """ + self.currentWeather.getCity() + """
                        </h1>
                    </div>
                <body>
                    <div class="container">
                        <div class="row">
                            <div class="col-sm-4">
                                <h3>Temperature</h3>
                                <p>""" + self.currentWeather.getTemperature() + ' C' + """</p>
                            </div>
                            <div class="col-sm-4">
                                <h3>Conditions</h3>
                                <p>""" + self.currentWeather.getWeatherConditions() + """</p>
                            </div>
                            <div class="col-sm-4">
                                <h3>Wind Speed</h3>
                                <p>""" + self.currentWeather.getWindSpeed() + ' mph' + """</p>
                            </div>
                        </div>
                          <div class="row">
                            <div class="col-sm-4">
                                <h3>Humidity</h3>
                                <p>""" + self.currentWeather.getHumidity() + '%' + """</p>
                            </div>
                            <div class="col-sm-4">
                                <h3>Sunrise</h3>
                                <p>""" + self.currentWeather.getSunrise() + """</p>
                            </div>
                            <div class="col-sm-4">
                                <h3>Sunset</h3>
                                <p>""" + self.currentWeather.getSunset() + """</p>
                            </div>
                        </div>
                  </div>
                </body>

                </html>
               """

if __name__ == "__main__":   
    cherrypy.config.update( {'server.socket_host': '0.0.0.0'} )
    cherrypy.config.update( {'server.socket_port': 80} )

    city_name = input("Enter a city Name : ")
    weather = WeatherData3(city_name)
    cherrypy.quickstart(Dashboard3(weather))
    
    