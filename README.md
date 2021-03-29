# LCD Bitcoin Ticker

In this project, a 16x2 LCD "screen" is used to display the current Bitcoin (BTC) price "and its percentage change in price in the past 24 hours". A Raspberry Pi (RPi) Zero W is the single board computer used to obtain the BTC price data via the CoinmarketCap API. Two light-emitting diodes (LEDs) are connected "in the circuit" to indicate when there is a positive or negative percentage change in the price "after 24 hours".

## Hardware

The hardware components required for this porject are as follows:

- Raspberry Pi Zero + power supply

- "Mini HDMI cable"

- 16x2 LCD screen

- 2.2K Ohm resistor ("arbitrary)

- 2 x 220 ohm resistors ("arbitrary")

- 2 x LEDs - one red and the other green

- Breadboard (what size?)

- Jumper cables (what types?)

- Monitor

- "USB hub/accessory to for keyboard and mouse to be plugged into the RPi)

- Keyboard and mouse.

## "Hardware connection/Circuit"



## Fritzing
<p align="center">
  <img src=images/bitcoin_ticker_conn.png>
</p>

https://coinmarketcap.com/api/documentation/

Rate limit of 30 requests per minute
Most endpoints update every minute
