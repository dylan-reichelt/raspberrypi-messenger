# raspberrypi-messenger

Name is a tad misleading. This application is a clock and weather display. It also has the capability to receive messages from a client and display
them underneath the clock. This is a good present for long distance relationships or anyone you want to send fun messages to. In order
to do this from seperate locations without opening ports and all that jazz you can utilize NGROK. I will not be showing how to do that
in this README, please look at their website: www.ngrok.com.

Items Recommended:

1) [Raspberry Pi](https://www.amazon.com/Raspberry-Model-Quad-Core-Bluetooth/dp/B08C4SK5C3/ref=sr_1_13?dchild=1&keywords=raspberry+pi+4&qid=1607539165&sr=8-13)

2) [7" Touchscreen](https://www.amazon.com/Raspberry-Pi-7-Touchscreen-Display/dp/B0153R2A9I/ref=sr_1_3?crid=2H2S8ZSI95LJB&dchild=1&keywords=7+inch+raspberry+pi+screen&qid=1607539205&sprefix=7inch+raspberry+pi%2Caps%2C211&sr=8-3)

3) [Touchscreen Case](https://www.amazon.com/Raspberry-Screen-Monitor-Touchscreen-Display/dp/B081VT2CPW/ref=sr_1_9?dchild=1&keywords=7+inch+raspberry+pi+screen+case&qid=1607539239&sr=8-9)

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3) Enter "WEATHER_API_KEY = <API KEY>"

You should be done. Then move on to usage and test.

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
