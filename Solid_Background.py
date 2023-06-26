# Relative path
import os

# Imports PIL module
from PIL import Image

# Import standard colours
import Colours

# VARIABLES
COLOUR_MODE = 'RGB'  # RGB, RGBA, CMYK, YCbCr, LAB, HSV...
COLOUR = Colours.White  # The colour of the image
SAVE_PATH = 'Images'  # Where to save the image
OUTPUT_NAME = 'white_square'  # What the new image should be named
SIZE = (300, 450)  # The dimensions of the new image
SHOW = True  # Show the image in the image viewer

directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(directory, SAVE_PATH)


def main():
    # Creating an image object with a certain size and colour
    image = Image.new(mode=COLOUR_MODE, size=SIZE, color=COLOUR)

    # Save image
    image.save(f"{path}\\{OUTPUT_NAME}_{SIZE[0]}_{SIZE[1]}.jpg", "JPEG")

    # Shows the image in the image viewer
    if SHOW:
        image.show()


if __name__ == '__main__':
    main()
