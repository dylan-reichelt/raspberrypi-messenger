
import sys
from pprint import pprint
from tkinter import *
from server import MyServer
import time
import threading
import os
from datetime import datetime
from MyWeather import MyWeather
from PIL import Image, ImageDraw, ImageFont

newOutput = False
output = ""
myServer = MyServer(sys.argv[1], sys.argv[2])

def applicationStart():
    apiweather = MyWeather()

    picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
    icondir = os.path.join(picdir, 'icon')
    fontdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'font')

    # Set the fonts
    font22 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 22)
    font30 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 30)
    font35 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 35)
    font50 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 50)
    font60 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 60)
    font100 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 100)
    font160 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 160)
    # Set the colors
    black = 'rgb(0,0,0)'
    white = 'rgb(255,255,255)'
    grey = 'rgb(235,235,235)'

    while(True):
        error_connect = True
        while error_connect:
            try:
                print('Attempting to connect to OWM.')
                response = apiweather.getWeatherData()
                print('Connection to OWM successful.')
                error_connect = False
            except:
                print('Connection error.')
                #TODO Display Error Message
            
        error = None
        while error == None:
            if response.status_code == 200:
                print('Connection to Open Weather successful.')
                # get data in json format
                data = response.json()
                print(data)
                
                # get current dict block
                current = data['main']

                current_temp = current['temp']
                
                feels_like = current['feels_like']

                humidity = current['humidity']

                wind = data['wind']['speed']

                weather = data['weather']
                report = weather[0]['description']
                icon_code = weather[0]['icon']

                temp_max = current['temp_max']
                temp_min = current['temp_min']
                    
                #TODO add location based from api response
                string_location = "CITY"
                string_temp_current = format(current_temp, '.0f') + u'\N{DEGREE SIGN}F'
                string_feels_like = 'Feels like: ' + format(feels_like, '.0f') +  u'\N{DEGREE SIGN}F'
                string_humidity = 'Humidity: ' + str(humidity) + '%'
                string_wind = 'Wind: ' + format(wind, '.1f') + ' MPH'
                string_report = 'Now: ' + report.title()
                string_temp_max = 'High: ' + format(temp_max, '>.0f') + u'\N{DEGREE SIGN}F'
                string_temp_min = 'Low:  ' + format(temp_min, '>.0f') + u'\N{DEGREE SIGN}F'

                error = False
            else:
                print(response)
                print("OH NO")

        # Open template file
        template = Image.open(os.path.join(picdir, 'template.png'))
        # Initialize the drawing context with template as background
        draw = ImageDraw.Draw(template)
    
        # Draw top left box
        ## Open icon file
        icon_file = icon_code + '.png' 
        icon_image = Image.open(os.path.join(icondir, icon_file))
        ### Paste the image
        template.paste(icon_image, (40, 15))
        ## Place a black rectangle outline
        draw.rectangle((25, 20, 225, 180), outline=black)
        ## Draw text
        draw.text((30, 200), string_report, font=font22, fill=black)
        # Draw top right box
        draw.text((375, 35), string_temp_current, font=font160, fill=black)
        draw.text((350, 210), string_feels_like, font=font50, fill=black)
        # Draw bottom left box
        draw.text((35, 325), string_temp_max, font=font50, fill=black)
        draw.rectangle((170, 385, 265, 387), fill=black)
        draw.text((35, 390), string_temp_min, font=font50, fill=black)
        # Draw bottom middle box
        draw.text((345, 340), string_humidity, font=font30, fill=black)
        draw.text((345, 400), string_wind, font=font30, fill=black)
        # Draw bottom right box
        draw.text((627, 330), 'UPDATED', font=font35, fill=white)
        current_time = datetime.now().strftime('%H:%M')
        draw.text((627, 375), current_time, font = font60, fill=white)

        ## Add Message
        global output
        global newOutput
        global myServer

        if(newOutput):
            myServer.setNewOutput(False)
            newOutput = False
            draw.rectangle((345, 13, 705, 55), fill =black)
            draw.text((355, 15), output, font=font30, fill=white)
        
        # Save the image for display as PNG
        screen_output_file = os.path.join(picdir, 'screen_output.png')
        template.save(screen_output_file)
        # Close the template file
        template.close()

        print('Writing to screen.')
        # Open the template
        with Image.open(os.path.join(picdir, screen_output_file)) as screen_output_file:
            # Initialize the drawing context with template as background
            screen_output_file.show()
            # Sleep
            print('Sleeping for ' + str(60) +'.')
            time.sleep(60)

def serverStart():
    global output
    global newOutput
    global myServer
    
    myServer.run()
    output = myServer.getOutput()
    newOutput = myServer.getNewOutput()
    serverStart()

thread = threading.Thread(target = serverStart)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    applicationStart()