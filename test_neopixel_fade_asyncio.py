# https://learn.adafruit.com/adafruit-esp32-s2-feather/multitasking-with-asyncio

# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
CircuitPython asyncio example for two NeoPixel rings and one button.
"""
from config import ledstrip_pin
import asyncio
import board
import neopixel
import keypad
from rainbowio import colorwheel

num_pixels = 16  # The number of NeoPixels on a single ring.
brightness = 0.2  # The LED brightness.

# Set up NeoPixel rings.
ring_one = neopixel.NeoPixel(ledstrip_pin, num_pixels, brightness=brightness, auto_write=False)

class AnimationControls:
    """The controls to allow you to vary the rainbow and blink animations."""
    def __init__(self):
        self.reverse = False
        self.wait = 0.0
        self.delay = 0.5

async def rainbow_cycle(controls):
    """Rainbow cycle animation on ring one."""
    while True:
        for j in range(255, -1, -1) if controls.reverse else range(0, 256, 1):
            for i in range(num_pixels):
                rc_index = (i * 256 // num_pixels) + j
                ring_one[i] = colorwheel(rc_index & 255)
            ring_one.show()
            await asyncio.sleep(controls.wait)



async def main():
    animation_controls = AnimationControls()
    animation_task = asyncio.create_task(rainbow_cycle(animation_controls))

    # This will run forever, because no tasks ever finish.
    await asyncio.gather(animation_task)

asyncio.run(main())