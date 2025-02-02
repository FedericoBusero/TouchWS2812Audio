# TouchWS2812Audio
A CircuitPython program that plays an MP3 and fades a WS2812 ledstrip after a capacitive touch event

# Before installation: install Circuitpython on your device
- Lolin S2 mini instruction
  - download the CircuitPython firmware .BIN file from https://circuitpython.org/board/lolin_s2_mini/
  - install the downloaded CircuitPython firmware using the online tool https://adafruit.github.io/Adafruit_WebSerial_ESPTool/
    Use the default settings (address 0)

# Pinout
- The pinout is defined in the config file. On lolin S2 mini this is using a I2S breakout board
  
| Function | Pin    |
| -------- | ------ |
| I2S SCLK | GPIO4  |
| I2S WS   | GPIO5  |
| I2S Data | GPIO18 |
| WS2812   | GPIO16 |
| Touch    | GPIO3  |

- The pinout of RP2040 is using the internal DAC
  
| Function | Pin    |
| -------- | ------ |
| Audio    | GPIO0  |
| WS2812   | GPIO15 |
| Touch    | GPIO3  |

# Installation
- copy all files (including the lib directory) to the circuitpython drive of your device
- rename the appropriate config file to config.py
e.g. when running the example on a Lolin S2 mini, rename config_lolin_s2.py to config.py
- copy the program you want to run to code.py
e.g. when you want to test the ledstrip, copy test_neopixel_fade_asyncio.py to code.py
The actual program that plays an MP3 and fades a WS2812 ledstrip after a capacitive touch event is touchWS2812Audio.py
