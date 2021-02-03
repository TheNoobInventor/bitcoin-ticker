"""

This program outputs the current Bitcoin (BTC) price and its 24 hour percentage change onto a 16x2 LCD screen. 
A green and red LED are used to indicate 24 hour price increases and decreases consecutively. 

"""

#--- Import packages.
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from time import sleep
import lcdlib as lcd
import RPi.GPIO as GPIO

#--- Define RAM addresses for the LCD.
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line/row of the LCD.
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line/row of the LCD.

#--- Initialize display.
lcd.init(25,24,23,17,18,22,16)

#--- GPIO pin setup.
"""
The following have been setup in the lcdlib package and do not need to be
declared again:

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

"""
amberLedPin = 27
redLedPin = 4
GPIO.setup(amberLedPin, GPIO.OUT)
GPIO.setup(redLedPin, GPIO.OUT)

#--- API endpoint to return the latest market quote for 1 or more cryptocurrencies from CoinmarketCap.
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

#--- Define the parameters to be appended to the url.
parameters = {
    'id': 1,
    'convert': 'USD'
}

#--- Define header information.
headers = {
    'Accepts': 'application/json', # Specifies the type of data to be sent back from the server.
    'X-CMC_PRO_API_KEY': 'API-KEY' # Replace 'API-KEY' with the key provided from CoinmarketCap.
}

#--- Initialize session object used to persist information across requests - headers in this case.
session = Session()
session.headers.update(headers)

#--- Try-Except-Finally block.
try:
    # Main loop.
    while 1:
        # Turn off LEDs.
        GPIO.output(amberLedPin, GPIO.LOW)
        GPIO.output(redLedPin, GPIO.LOW)

        # Data retrieval and formatting.
        response = session.get(url, params=parameters) # Retrieve latest quote data with the url and parameters specified.
        data = json.loads(response.text) # Convert the json response data into a python dictionary.
        price = int(data['data']['1']['quote']['USD']['price']) # Retrieve current BTC price.
        price = str("{:,}".format(price)) # Convert BTC price into a string.
        percent_change = (data['data']['1']['quote']['USD']['percent_change_24h']) # Retrieve 24 hr percentage change data.
        percent_change_str = str("{:.2f}".format(percent_change)) # Convert perctage change into a string.

        # LCD outputs.
        lcd.string("BTC: $"+price, LCD_LINE_1) # Output current BTC price on first row of the LCD.
        sleep(0.2)
        lcd.string("24hr del: " +percent_change_str+"%", LCD_LINE_2) # Output 24hr price percentage change on the second row of the LCD.

        # Turn on amber LED if 24hr price percentage change is positive. Or
        # turn on red LED if the percentage change is negative.
        if percent_change > 0:
            GPIO.output(amberLedPin, GPIO.HIGH)
        else:
            GPIO.output(redLedPin, GPIO.HIGH)

        # Add delay to request an update every minute.
        sleep(60)

# Request exceptions, for debugging purposes.
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# Handle KeyboardInterrupt exception when the program is ended by executing Ctrl-C.
except KeyboardInterrupt:
    # Clear lcd screen.
    lcd.string("", LCD_LINE_1)
    lcd.string("", LCD_LINE_2)

finally:
    # Clean up GPIO pins.
    GPIO.cleanup()
