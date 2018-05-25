# Project_Oracle
## Objective:
To create a piece of software that is able to pull weather information and display it through the serial port of a Raspberry Pi.

## Setup:
1. Install the dependencies:
  ```
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install python python3 python-pip python3-pip
  pip install google-api-client
  pip3 install google-api-client
  ```
  If you are on a Raspberry Pi and intend to use an I2C OLED display, go to https://github.com/adafruit/Adafruit_Python_SSD1306 to install the display libs.
2. Download this program:
  Open terminal. Go to the directory you want this downloaded, then type the following:
  ```
  git clone https://github.com/GeneralLol/Duanaweather.git
  ```
3. Go to Duanaweather:
  ```
  cd Duanaweather
  ```
4. Run help file:
  ```
  python3 Duanaweather -h
  ```

 ## End Result:
 The program should display date, time, weather and temperature to the display hooked up.

 ## OS Support:
 Currently the full function is only achieved (and tested) on Ubuntu.
 On a Raspberry Pi, WeatherModule doesn't work, and I2C display works.

 ## Current Issues:
 The Virtual Display is made using pygame, which takes a lot of sys resources. Considering about switching to PyQt.
 The Weather Module doesn't work on a Raspberry Pi due to some json operation issues.
# Duanaweather-2.0
