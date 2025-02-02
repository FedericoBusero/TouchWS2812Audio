from config import ledstrip_pin,num_pixels
import asyncio
import neopixel

brightness = 0.2  # The LED brightness.

# Set up NeoPixel ledstrip
ledstrip = neopixel.NeoPixel(ledstrip_pin, num_pixels, brightness=brightness, auto_write=False)

async def fade_cycle(time_wait,time_delay,num):
    """Fade cycle animation on led strip."""
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


async def main():
    animation_task = asyncio.create_task(fade_cycle(0.002,0.5,30))

    # This will run forever, because no tasks ever finish.
    await asyncio.gather(animation_task)

asyncio.run(main())
