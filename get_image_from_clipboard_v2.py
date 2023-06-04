from PIL import ImageGrab, Image
from datetime import datetime
import time


def get_image(img):
    # img = ImageGrab.grabclipboard()
    # print(img)
    # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=200x71 at 0x105E68700>

    # print(isinstance(img, Image.Image))
    # True

    if isinstance(img, Image.Image):
        # print(img.size)
        # (200, 71)

        # print(img.mode)
        # RGB

        image_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        img.save(image_file_name)
        print(f'Image was saved as {image_file_name}')
    else:
        # print('Image not found!')
        pass


def main():
    img = ''
    print('Get image from clipboard is running ...')
    while True:
        while (img == ImageGrab.grabclipboard()):
            time.sleep(1)
        img = ImageGrab.grabclipboard()
        get_image(img)


if __name__ == '__main__':
    main()