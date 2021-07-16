# Lcd Bitcoin Ticker

In this project, a 16x2 Liquid Crystal Display (LCD) screen is used to display the current Bitcoin (BTC) price and its percentage price change in the past 24 hours. A Raspberry Pi (RPi) Zero W is the single board computer used to obtain the BTC price data via the CoinmarketCap API. Two light-emitting diodes (LEDs) are connected in a circuit on a breadboard to indicate either a positive or negative percentage price change in the past 24 hours.

## Hardware

### Components

The hardware components required for this project are as follows:

- Raspberry Pi Zero + power supply

- Mini HDMI cable

- 16x2 LCD screen

- 5K Ohm trimmer potentiometer

- 2 x 220 ohm resistors

- 2 x LEDs - one red and the other green (however an amber LED was used in place of the green)

- Full sized breadboard

- Jumper cables: male-male, female-male dupoint cables

- Monitor

- USB hub/accessory for the keyboard and mouse to be plugged into the RPi

- Keyboard and mouse.

### Project wiring

The wiring for the project is shown in the figure below.

<p align="center">
  <img src=images/bitcoin_ticker_fritz.png>
</p>

Jumper cables are used in connecting the LCD screen, Raspberry Pi Zero and the LEDs together. The LCD pin onnections are as follows:

LCD pin 1 > GND

LCD pin 2 > 5V

LCD pin 3 > GND

LCD pin 4 > GPIO 25

LCD pin 5 > GND

LCD pin 6 > GPIO 24

LCD pin 7 to 10 > No connections

LCD pin 11 > GPIO 23

LCD pin 12 > GPIO 17

LCD pin 13 > GPIO 18

LCD pin 14 > GPIO 22

LCD pin 15 > 5V

LCD pin 16 > GND

Pin 3 of the LCD is connected in line with a 5K Ohm trimmer potentiometer to dim the display for legibility. The green and red LEDs, connected in line with 220 Ohm resistors, are connected to the RPi pins GPIO27 and GPIO4 consecutively.

The following pictures show the components fully assembled. 

<p align="center">
  <img src=images/top_view_assembled.jpg>
</p>

<p align="center">
  <img src=images/side_view.jpg>
</p>

<p align="center">
  <img src=images/angled_view.jpg>
</p>

After assembling the project, the next step is to install the operating system and clone this repository.

## Software

**Raspberry Pi OS** is the operating system running on the Raspberry Pi Zero W. The download and installation procedures are detailed [here](https://www.raspberrypi.org/software/). 

This repository contains a well commented `main.py` file for this project is written in **Python 3** and makes use of LCD library in the file `lcdlib.py`. The LCD library in use can be found [here](https://www.hackster.io/trduunze/raspberry-pi-lcd-screen-339eb5).

The LCD is initialized in line 21 in `main.py`, with the LCD pins declared earlier, as follows:

```
lcd.init(25,24,23,17,18,22,16)
````

The BTC price and percentage change data are now required. The CoinMarketCap Application Programming Interface (API) is used to obtain this information that will be outputted to the LCD.

### CoinMarketCap Api

An API key is needed to access the data required by `main.py` file. A basic API plan, created and accessed [here](https://coinmarketcap.com/api/) will suffice for this project. With this plan, 30 API requests can be made per minute and depending on the endpoints (data available such as fiat currencies, cryptocurrencies and more) chosen, updates can be expected every minute.

The python example shown in the [quick start guide](https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide) was adapted and used in this project. In the following code block, lines 47 to 50 in `main.py`, 'API-KEY' is replaced by the API key provided by CoinMarketCap.


```
headers = {
    'Accepts': 'application/json', # Specifies the type of data to be sent back from the server.
    'X-CMC_PRO_API_KEY': 'API-KEY' # Replace 'API-KEY' with the key provided by CoinmarketCap.
} 
```


After the API key substitution, the program is executed by running the following command in the terminal:


```
python main.py
```

The image below shows an output of the main program on the LCD, with the amber LED indicating a positive price change over the past 24 hours.

<p align="center">
  <img src=images/top_view_code_running.jpg>
</p>

## Video demonstration

The following video walks through the API setup process, and runs `main.py` to output the BTC price and its 24 hour percentage change on the LCD.

(to be done)

## References
- [Raspberry Pi LCD screen](https://www.hackster.io/trduunze/raspberry-pi-lcd-screen-339eb5)

- [CoinmarketCap Docs](https://coinmarketcap.com/api/documentation/)
