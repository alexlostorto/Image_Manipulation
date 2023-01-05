# Importing Image class from PIL module
from PIL import Image

# VARIABLES
IMAGE_EXTENSION = '.jpg'
IMAGE_NAME = 'bauble'
FILE_PATH = f'Cropped\\{IMAGE_NAME}'
SAVE_PATH = 'Merged'
OUTPUT_NAME = 'bauble'
IMAGES = 2  # Number of images to merge
HORIZONTAL = True  # True to merge horizontally


def main():
    image_list = []

    for i in range(IMAGES):
        image = Image.open(f"{FILE_PATH}{i + 1}{IMAGE_EXTENSION}")
        image_list.append(image)

    # Create new merged image
    if HORIZONTAL:
        new_image = Image.new('RGB', (IMAGES * image_list[0].size[0], image_list[0].size[1]), (250, 250, 250))
    else:
        new_image = Image.new('RGB', (image_list[0].size[0], IMAGES * image_list[0].size[1]), (250, 250, 250))

    x, y = 0, 0
    for i in range(IMAGES):
        if HORIZONTAL:
            new_image.paste(image_list[i], (x, 0))
        else:
            new_image.paste(image_list[i], (0, y))
        x += image_list[i].size[0]
        y += image_list[i].size[1]

    new_image.save(f"{SAVE_PATH}\\{OUTPUT_NAME}.jpg", "JPEG")
    new_image.show()


if __name__ == '__main__':
    main()
