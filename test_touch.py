from config import *
#import board
import touchio
import asyncio

# Set up the touch input
touch = touchio.TouchIn(touch_pin)

async def touch_calib_task():
    mintouch = touch.raw_value
    for x in range(100):
        print(mintouch)
        mintouch = min(mintouch,touch.raw_value)
        await asyncio.sleep(0.1)
    print("calibrating end")
    touch.threshold = mintouch + 100


async def touch_task():
    while True:
        if touch.value:
            builtinled_on()
        else:
            builtinled_off()
        await asyncio.sleep(0.1)

async def main():
    touch_task_coro = touch_task()
    await asyncio.sleep(0.5)
    touch.threshold = touch.raw_value + 100
#    touch_task_log = touch_calib_task()
#    await asyncio.gather(touch_task_coro,touch_task_log)
    await asyncio.gather(touch_task_coro)

# Run the main function
asyncio.run(main())
