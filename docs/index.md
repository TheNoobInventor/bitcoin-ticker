# LCD Bitcoin Ticker

In this project, a 16x2 LCD screen is used to display the current Bitcoin (BTC) price and its percentage change in price in the past 24 hours. A Raspberry Pi (RPi) Zero W is the single board computer used to obtain the BTC price data via the CoinmarketCap API. Two light-emitting diodes (LEDs) are connected in a circuit on a breadboard to indicate a positive or negative percentage change in the price after 24 hours.

(to be completed)

## Hardware

### Components

The hardware components required for this project are as follows:

- Raspberry Pi Zero + power supply

- Mini HDMI cable

- 16x2 LCD screen

- 5K Ohm trimmer potentiometer

- 2 x 220 ohm resistors

- 2 x LEDs - one red and the other green

- Full sized breadboard

- Jumper cables: male-male, female-male dupoint cables

- Monitor

- USB hub/accessory to for keyboard and mouse to be plugged into the RPi)

- Keyboard and mouse.

### Project Wiring

The wiring for the project is shown in the figure below.

<p align="center">
  <img src=images/bitcoin_ticker_fritz.png>
</p>

The jumper cables are used in connecting the LCD screen, Raspberry Pi Zero and the LEDs as follows:

LCD pin 1 > GND

LCD pin 2 > 5V

LCD pin 3 > GND

LCD pin 4 > GPIO 25

LCD pin 5 > GND

LCD pin 6 > GPIO 24

LCD pin 7 - 10 > No connections

LCD pin 11 > GPIO 23

LCD pin 12 > GPIO 17

LCD pin 13 > GPIO 18

LCD pin 14 > GPIO 22

LCD pin 15 > 5V

LCD pin 16 > GND

Pin 3 of the LCD is connected in line with a 5K Ohm trimmer potentiometer to dim the display for legibility. The green and red LEDs are connected to the RPi pins GPIO27 and GPIO4 consecutively to be controlled in the python code. "220 Ohm resistors are connected in line with the LEDs."

More information about the LCD pinout can be obtained [here](https://www.hackster.io/trduunze/raspberry-pi-lcd-screen-339eb5).

"assembled below"

<p align="center">
  <img src=images/top_view.jpg>
</p>

<p align="center">
  <img src=images/side_view.jpg>
</p>

<p align="center">
  <img src=images/angled_view.jpg>
</p>

## Software

### Software architecture

**Raspberry Pi OS** is the operating system used on the Raspberry Pi 4. The download and installation procedure can be found [here](https://www.raspberrypi.org/software/). **Python 3** and the lcd library

where I got the library (or have a separate link for the lib?):
https://www.hackster.io/trduunze/raspberry-pi-lcd-screen-339eb5

explain installation procedure for the library

Edit below::
Before we start programming we need to install a library I created [here](https://github.com/Grant-P-W/lcd_lib). To do this, we must first go there and download the library as a zip folder. Then, extract it to wherever you want using the archive manager. Now we have to open the terminal to move the file to the correct location. Let's use the mv command for this. Just type or copy the following into your terminal replacing `/home/pi/Wherever_You_Extracted_Your_Folder_To/lcd_lib-master/lcdlib.py` with the path to the lcdlib.py file.

`sudo mv -v /home/pi/Wherever_You_Extracted_Your_Folder_To/lcd_lib-master/lcdlib.py /usr/lib/python3.4`
If you use a different virsion of python, that is, python2.7, replace the python3.4 to whatever version you use.


The code is rather easy. At the beginning of each script, you must import the library by typing: import lcdlib as lcd . Then, remember to define your RAM addresses, in my case:

`LCD_LINE_1 = 0x80`

`LCD_LINE_2 = 0xC0`
Now the last bit of initialization is the lcd.init() function, which we talked about earlier.

Now you can use the lcd.string() to display your text.

### Software install/setup
how to download and run the code


### CoinmarketCap API

get your api key https://coinmarketcap.com/api/


## Video demonstration
Check snake_game README for thumbnail


## Observations
If you use the Raspberry Pi Logo in this way on a website, the logo must link to our website at http://www.raspberrypi.org

Mention python example for using coinmarketcap api

[CoinmarketCap Docs](https://coinmarketcap.com/api/documentation/)


Rate limit of 30 requests per minute
Most endpoints update every minute

where to mention that the main.py file is the "main" file. talk about cloning the repo or are we just assuming that they should know. But write a line or two to make it accessible to any newbie (that's what we are pushing for).

## References
