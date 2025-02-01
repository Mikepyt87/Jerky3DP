import time
import board
from rainbowio import colorwheel
import neopixel

# Update this to match the pin to which you connected the NeoPixels
pixel_pin = board.A3
# Update this to match the number of NeoPixels connected
num_pixels = 44

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
# Set to 0-1 to change the brightness of the NeoPixels
pixels.brightness = .25

def rainbow_cycle(wait):
    """Rainbow cycle animation. Cycles across all pixels."""
    for color_index in range(255):
        for pixel in range(num_pixels):
            pixel_index = (pixel * 256 // num_pixels) + color_index
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    # Rainbow cycle.
    rainbow_cycle(0)  # Increase the number to slow down the rainbow.
