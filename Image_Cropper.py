# Importing Image class from PIL module
from PIL import Image

# VARIABLES
IMAGE_NAME = 'test1.jpeg'  # The name of the image being cropped
FILE_PATH = f'Images\\{IMAGE_NAME}'  # Where the original image is located
OUTPUT_NAME = 'bauble'  # What the new image should be named
SAVE_PATH = 'Cropped'  # Where to save the images
ALIGN = 'centre'  # Top, bottom, left, right, centre is default
SQUARES = 2  # Number of squares to split the image into
HORIZONTAL = True  # True to split image on x-axis
SHOW = False  # Show each image in the image viewer


def main():
    # Opens a image in RGB mode
    image = Image.open(FILE_PATH)

    # Size of the image in pixels
    width, height = image.size

    if HORIZONTAL:  # Split image along x-axis
        lengths = [width, height]
    else:  # Split image along along y-axis
        lengths = [height, width]

    square_size = lengths[0] // SQUARES
    gap = lengths[1] - square_size

    # Makes sure the square isn't bigger than the height of the image
    if square_size > height:
        square_size = height

    if HORIZONTAL:  # Centre squares along the y-axis
        top = gap // 2
        bottom = height - gap // 2
        left = 0
        right = width
    else:  # Centre squares along the x-axis
        top = 0
        bottom = height
        left = gap // 2
        right = width - gap // 2

    # Setting the points for cropped image
    if ALIGN.lower() == 'top':
        top = 0
        if HORIZONTAL:
            bottom = square_size
        else:
            bottom = height - square_size * SQUARES
    elif ALIGN.lower() == 'bottom':
        bottom = height
        if HORIZONTAL:
            top = height - square_size
        else:
            top = height - square_size * SQUARES
    elif ALIGN.lower() == 'left':
        left = 0
        if HORIZONTAL:
            right = square_size * SQUARES
        else:
            right = width - square_size
    elif ALIGN.lower() == 'right':
        right = width
        if HORIZONTAL:
            left = width - square_size * SQUARES
        else:
            left = width - square_size

    for i in range(SQUARES):
        if HORIZONTAL:
            left = square_size * i
            right = width - square_size * (SQUARES - (i + 1))
        else:
            top = square_size * i
            bottom = height - square_size * (SQUARES - (i + 1))

        # Debugging
        print(f"Top: {top}")
        print(f"Bottom: {bottom}")
        print(f"Left: {left}")
        print(f"Right: {right}")
        print(f"Width: {width}")
        print(f"Height: {height}\n")

        # Cropped image with dimensions above
        cropped = image.crop((left, top, right, bottom))

        # Save image
        cropped.save(f"{SAVE_PATH}\\{OUTPUT_NAME}{i+1}.jpg", "JPEG")

        # Shows the image in the image viewer
        if SHOW:
            cropped.show()


if __name__ == '__main__':
    main()
