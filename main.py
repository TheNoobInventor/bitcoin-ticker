#--- Import packages
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from time import sleep
import lcdlib as lcd
import RPi.GPIO as GPIO

#---
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

#--- Initialize display
lcd.init(25,24,23,17,18,22,16)


#---
#GPIO.setmode(GPIO.BCM) already set inlcdlib
GPIO.setwarnings(False)
greenLedPin = 14 #17 #38
redLedPin = 15 #27 #40
GPIO.setup(greenLedPin, GPIO.OUT)
GPIO.setup(redLedPin, GPIO.OUT)

#---
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'id': 1,
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'e3f4e07f-e1ba-4ae2-a368-32caafafa1ca'
}

#---
session = Session()
session.headers.update(headers)

#---
try:
    while 1:
        #
        GPIO.output(greenLedPin, GPIO.LOW)
        GPIO.output(redLedPin, GPIO.LOW)
        
        #
        response = session.get(url, params=parameters)
        received = json.loads(response.text) # choose better name
        price = int(received['data']['1']['quote']['USD']['price'])
        price = str("{:,}".format(price))
        percent_change = (received['data']['1']['quote']['USD']['percent_change_24h'])# 24 hr percentage change
        percent_change_str = str("{:.2f}".format(percent_change))
        
        #
        lcd.string("BTC: $"+price, LCD_LINE_1)
        sleep(0.2)
        lcd.string("24hr del: " +percent_change_str+"%", LCD_LINE_2)
        
        #
        if percent_change > 0:
            GPIO.output(greenLedPin, GPIO.HIGH)
        else:
            GPIO.output(redLedPin, GPIO.HIGH)
        
        sleep(15) # why this?

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# think the data updates every 60 seconds..confirm
# Add keyboard interrupt
# Polish up and comment code
# is try-while-except a good way of coding this?
# percentage change and link it to LEDs or fash for now
# hide the key I used or just use a filler so that people can sign up for theirs or use a "free" key in the readme