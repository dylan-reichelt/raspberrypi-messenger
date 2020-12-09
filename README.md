# raspberrypi-messenger

Name is a tad misleading. This application is a clock and weather display (based off of [this](https://github.com/AbnormalDistributions/e_paper_weather_display)). It also has the capability to receive messages from a client and display
them underneath the clock. This is a good present for long distance relationships or anyone you want to send fun messages to. In order
to send messages from seperate networks without opening ports and all that jazz you can utilize NGROK. I will not be showing how to do that
in this README, please look at their website: www.ngrok.com.

Items Recommended:

1) [Raspberry Pi](https://www.amazon.com/Raspberry-Model-Quad-Core-Bluetooth/dp/B08C4SK5C3/ref=sr_1_13?dchild=1&keywords=raspberry+pi+4&qid=1607539165&sr=8-13)

2) [7" Touchscreen](https://www.amazon.com/Raspberry-Pi-7-Touchscreen-Display/dp/B0153R2A9I/ref=sr_1_3?crid=2H2S8ZSI95LJB&dchild=1&keywords=7+inch+raspberry+pi+screen&qid=1607539205&sprefix=7inch+raspberry+pi%2Caps%2C211&sr=8-3)

3) [Touchscreen Case](https://www.amazon.com/Raspberry-Screen-Monitor-Touchscreen-Display/dp/B081VT2CPW/ref=sr_1_9?dchild=1&keywords=7+inch+raspberry+pi+screen+case&qid=1607539239&sr=8-9)

## Pictures

<ins>No Message Displayed:</ins>

<img src="https://github.com/dylan-reichelt/raspberrypi-messenger/blob/master/example_pics/home_nomessage" width=40% height=40%>


<ins>Message Displayed:</ins>

<img src="https://github.com/dylan-reichelt/raspberrypi-messenger/blob/master/example_pics/homescreen_message.png" width=40% height=40%>

## Installation

Open Weather API Needed, as well as other misc. items:

```bash
pip install openweather
pip install pygame
pip install Pillow
```

Once these are all installed you will need to put your OpenWeather API Key into a constant file.
Follow these steps for that:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1) Obtain OpenWeatherAPI Key: https://openweathermap.org/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2) Create constant.py file in the server directory

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3) Enter "WEATHER_API_KEY = [Your API Key]"

You should be done. Then move on to usage and test.

## Usage

<ins>Server:</ins>

format:
```bash
python3 main.py <host> <port> <zipcode>
```

Example:

```bash
cd server/
python3 main.py localhost 4556
```

```bash
cd server/
python3 main.py localhost 4556 85251
```

NOTE: Zipcode is optional. It is used to gather weather data about that location. Default value is 91604 (Studio City).

<ins>Client:</ins>

format:
```bash
python3 main.py <host> <port> <message>
```

Example:

```bash
cd client/
python3 main.py localhost 4556 "This is a test"
```
Response from server:

```bash
connecting to localhost port 4556
sending 'This is a test'
Message sent successfully :D
closing socket
```

## Optional Steps

<ins>Shortcut for automated start:</ins>

1) right-click and hit "create shortcut" for start.sh

2) Drag that shortcut wherever you wish

3) Double click and it should start the application

NOTE: This is automating an ngrok TCP tunnel processes as well. The tunnel is connected to localhost port 4556. In order to get NGROK working go to www.ngrok.com.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
