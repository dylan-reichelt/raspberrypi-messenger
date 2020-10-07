
import sys
from pprint import pprint
from tkinter import *
from server import MyServer
import time
import threading
import os
import pygame
from datetime import datetime
from MyWeather import MyWeather
from PIL import Image, ImageDraw, ImageFont

output = ""
myServer = MyServer(sys.argv[1], sys.argv[2])

def timeConvert(timeIn):
    hours, minutes = timeIn.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "am"
    if hours > 12:
        setting = "pm"
        hours -= 12
    return ("%02d:%02d" + setting) % (hours, minutes)

def applicationStart():
    pygame.init()
    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((800, 480))
    apiweather = MyWeather()

    pastoutput = "past"

    if len(sys.argv) > 3:
        apiweather.setZipCode(sys.argv[3])
        
    pasttime = timeConvert(datetime.now().strftime("%H:%M"))
    string_current_time = timeConvert(datetime.now().strftime("%H:%M"))
    first = True

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
        while error_connect == True:
            try:
                if(pasttime != string_current_time or first == True):
                    print('Attempting to connect to OWM.')
                    response = apiweather.getWeatherData()
                    print('Connection to OWM successful.')
                    pasttime = string_current_time
                    first = False
                    print(response.json())
                error_connect = False
            except:
                print('Connection error.')
                #TODO Display Error Message
            
        error = None
        while error == None:
            if response.status_code == 200:
                # get data in json format
                data = response.json()
                
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
                    
                string_location_city = data['name']
                string_temp_current = format(current_temp, '.0f') + u'\N{DEGREE SIGN}F'
                string_feels_like = 'Feels like: ' + format(feels_like, '.0f') +  u'\N{DEGREE SIGN}F'
                string_humidity = 'Humidity: ' + str(humidity) + '%'
                string_wind = 'Wind: ' + format(wind, '.1f') + ' MPH'
                string_report = 'Now: ' + report.title()
                string_temp_max = 'High: ' + format(temp_max, '>.0f') + u'\N{DEGREE SIGN}F'
                string_temp_min = 'Low:  ' + format(temp_min, '>.0f') + u'\N{DEGREE SIGN}F'

                error = False
            else:
                error = True
        
        string_current_time = timeConvert(datetime.now().strftime("%H:%M"))
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
        ## Draw text
        draw.text((30, 200), string_report, font=font22, fill=black)
        draw.text((30, 230), string_temp_max, font=font22, fill=black)
        draw.text((30, 260), string_temp_min, font=font22, fill=black)
        # Draw top right box
        global output

        if "pm" in string_current_time:
            tempTime = string_current_time.replace("pm","")
            draw.text((325, 35), tempTime, font=font160, fill=black)
            draw.text((725, 150), "pm", font=font35, fill=black)
        
        elif "am" in string_current_time:
            tempTime = string_current_time.replace("am","")
            draw.text((325, 35), tempTime, font=font160, fill=black)
            draw.text((725, 150), "am", font=font35, fill=black) 

        draw.text((270, 220), output, font=font30, fill=black)
        # Draw bottom left box
        draw.text((110, 325), string_temp_current, font=font50, fill=black)
        draw.text((35, 400), string_feels_like, font=font35, fill=black)
        # Draw bottom middle box
        draw.text((345, 340), string_humidity, font=font30, fill=black)
        draw.text((345, 400), string_wind, font=font30, fill=black)
        # Draw bottom right box
        draw.text((610, 330), 'Location: ', font=font22, fill=white)
        draw.text((610, 375), string_location_city, font = font22, fill=white)
        
        # Save the image for display as PNG
        if(pasttime != string_current_time or pastoutput != output):
            print("Loading and saving new file!")
            screen_output_file = os.path.join(picdir, 'screen_output.png')
            template.save(screen_output_file)
            image0 = pygame.image.load(os.path.join(picdir, 'screen_output.png'))
            pastoutput = output

        
        # Close the template file
        template.close()
        screen.fill((0,0,0))
        screen.blit(image0,(0,0))
        

        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit() 
              
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
              
                #if the mouse is clicked on the 
                # button the game is terminated 
                if 725 <= mouse[0] <= 725+100 and 15 <= mouse[1] <= 15+40: 
                    pygame.quit()
                    sys.exit()
        
        color = (0,0,0) 
        smallfont = pygame.font.SysFont('Corbel',35) 
        quitText = smallfont.render('quit' , True , color)
        screen.blit(quitText , (725,15))

        mouse = pygame.mouse.get_pos()  
        pygame.display.update()

def serverStart():
    global output
    global myServer
    
    myServer.run()
    output = myServer.getOutput()
    serverStart()

thread = threading.Thread(target = serverStart)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    applicationStart()