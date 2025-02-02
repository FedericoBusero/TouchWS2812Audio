import board
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!
import neopixel

ledstrip_pin = board.GP15
num_pixels = 8
audio_output = AudioOut(board.GP0)
touch_pin = board.GP3

# Set up the NeoPixel
pixel_pin = board.GP16
pixels = neopixel.NeoPixel(pixel_pin, 1)

def builtinled_on():
    pixels[0] = (255, 0, 0)  # Red when touched

def builtinled_off():
    pixels[0] = (0, 0, 0)  # Off when not touched
