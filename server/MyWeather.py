import time
import requests
import constant
import json
from pprint import pprint

class MyWeather():
    def __init__(self):
        self.settings = {
            'api_key': constant.WEATHER_API_KEY,
            'zip_code':'91604',
            'country_code':'us',
            'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

    def getWeatherData(self):
        final_url = self.BASE_URL.format(self.settings["api_key"],self.settings["zip_code"],self.settings["country_code"],self.settings["temp_unit"])
        weather_data = requests.get(final_url)
        return weather_data
        
    
    def setZipCode(self, zipCode):
        self.settings["zip_code"] = zipCode
