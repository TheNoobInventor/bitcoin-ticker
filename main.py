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
greenLedPin = 27 # 14 #17 #38
redLedPin =4 #27 #40
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
    'X-CMC_PRO_API_KEY': 'API-KEY' # Replace 'API-KEY' with the key provided from Coinmarketcap
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
        
        # Add delay to request an update every minute
        sleep(60)

#        
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

#    
except KeyboardInterrupt:
    
    # Clear lcd screen
    lcd.string("", LCD_LINE_1)
    lcd.string("", LCD_LINE_2)

# is a comment necessary?    
finally:
    
    # Clean up GPIO pins   
    GPIO.cleanup()

# Rate limit of 30 requests per minute
# Most endpoints update every minute
# So we are adding 55 second delay not to request a lot since we are on the basic api plan
# Polish up and comment code. Have consistent commenting style
# hide the key I used or just use a filler so that people can sign up for theirs or use a "free" key in the readme
