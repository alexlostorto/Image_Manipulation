# Imports PIL module
from PIL import Image

# Import standard colours
import Colours

# VARIABLES
COLOUR_MODE = 'RGB'  # RGB, RGBA, CMYK, YCbCr, LAB, HSV...
COLOUR = Colours.Black  # The colour of the image
SAVE_PATH = 'Images'  # Where to save the image
OUTPUT_NAME = 'Black_Square'  # What the new image should be named
SIZE = (200, 200)  # The dimensions of the new image
SHOW = True  # Show the image in the image viewer


def main():
    # Creating an image object with a certain size and colour
    image = Image.new(mode=COLOUR_MODE, size=SIZE, color=COLOUR)

    # Save image
    image.save(f"{SAVE_PATH}\\{OUTPUT_NAME}_{SIZE[0]}_{SIZE[1]}.jpg", "JPEG")

    # Shows the image in the image viewer
    if SHOW:
        image.show()


if __name__ == '__main__':
    main()
    