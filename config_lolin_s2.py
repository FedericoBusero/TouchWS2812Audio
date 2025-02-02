import board
import audiobusio
import digitalio

print("Hello world from boot.py")

#class audiobusio.I2SOut(bit_clock: microcontroller.Pin, word_select: microcontroller.Pin, data: microcontroller.Pin, *,
# main_clock: microcontroller.Pin | None = None, left_justified: bool = False)

audio_output = audiobusio.I2SOut(board.IO4, board.IO5, board.IO18)
ledstrip_pin = board.IO16
touch_pin = board.IO3

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def builtinled_on():
    led.value = True

def builtinled_off():
    led.value = False
