import tkinter as tk
from MyWeather import MyWeather
from guizero import App, Text

class gui:

    def __init__(self):
        self.app = App(title = "Hello World")
        self.weather = MyWeather()
        self.message = Text(self.app, text = "Welcome to the Hello World App!")
        self.weatherUpdate = Text(self.app, text = self.weather.getWeatherData())
        self.messageOfTheDay = Text(self.app, text = "")
    
    def startGui(self):
        self.app.display()

    def greet(self):
        print("Greetings!")
    
    def getUpdatedWeather(self):
        print("UPDATING WEATHER")
        return self.weather.getWeatherData()
    
    def updateMessage(self, message):
        print("UPDATING Message")
        self.messageOfTheDay = Text(self.app, text = message)

