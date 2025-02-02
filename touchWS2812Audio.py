from config import *

#import board
import touchio
import asyncio
import neopixel
#import keypad
from rainbowio import colorwheel

import digitalio
from audiomp3 import MP3Decoder

mp3filename = "tardis.mp3"

num_pixels = 8
ledstrip = neopixel.NeoPixel(ledstrip_pin, num_pixels, brightness=0.2, auto_write=False)

# Set up the touch input
touch = touchio.TouchIn(touch_pin)

async def touch_calibrate():
    print("touch calibrate")
    for x in range(5):
        #warming up
        print(touch.raw_value)
        await asyncio.sleep(0.1)
    mintouch = touch.raw_value
    await asyncio.sleep(0.1)
    for x in range(10):
        #print("                  calib",mintouch)
        mintouch = min(mintouch,touch.raw_value)
        await asyncio.sleep(0.1)
    touch.threshold = mintouch + 50
    print("calibrating end, threshold ",touch.threshold)

async def fade_cycle(time_wait,time_delay,num):
    """Rainbow cycle animation on led strip."""
    for count in range(0, num):
        print("rainbow_cycle",count)
        for j in range(0, 256, 1):
            for i in range(num_pixels):
                ledstrip[i] = (j, 0, 0)
            ledstrip.show()
            await asyncio.sleep(time_wait)
        for j in range(255, -1, -1):
            for i in range(num_pixels):
                ledstrip[i] = (j, 0, 0)
            ledstrip.show()
            await asyncio.sleep(time_wait)
        await asyncio.sleep(time_delay)
        
    for i in range(num_pixels):
        ledstrip[i] = (0, 0, 0)
    ledstrip.show()

async def play_mp3(filename,num):
    for count in range(0, num):
        print("play_mp3",count)
        mp3 = open(filename, "rb")
        decoder = MP3Decoder(mp3)
        audio_output.play(decoder)
        while audio_output.playing:
            await asyncio.sleep(0.1)


async def main():
    print("started")
    calibrate = asyncio.create_task(touch_calibrate())
    await asyncio.gather(calibrate)

    while True:
        print(touch.raw_value," thresh:",touch.threshold)
        if touch.value:
            print("touched")
            builtinled_on()
            animation_task = asyncio.create_task(fade_cycle(0.002,0.5,4))
            music_task = asyncio.create_task(play_mp3(mp3filename,2))
            await asyncio.gather(animation_task,music_task)
            await asyncio.sleep(2)
            calibrate = asyncio.create_task(touch_calibrate())
            await asyncio.gather(calibrate)
        else:
            builtinled_off()
        await asyncio.sleep(0.1)

asyncio.run(main())

