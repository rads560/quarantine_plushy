import time
import board
import neopixel
from matplotlib import colors

pixel_pin = board.D18
num_pixels = 30
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, brightness=0.2, pixel_order=ORDER)
colormap = colors.Colormap

# Display the color specified by colorname on the LED strip
# See available color names here: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
def display_color(colorname):
	rgb_tuple = colors.to_rgb(colorname)
	scaled_tuple = tuple(255 * c for c in rgb_tuple)
	# print(scaled_tuple)
	pixels.fill(scaled_tuple)
	pixels.show()
	time.sleep(1)

while True:
	color = input("Please enter a color name: \n")
	display_color(color)