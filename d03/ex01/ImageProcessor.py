import numpy as np
from PIL import Image


class ImageProcessor():
    def __init__(self):
        pass

    def load(self, path):
        try:
            image = Image.open(path)
            print("Image size is :", image.size)
            data = np.asarray(image)
            return(data)
        except Exception:
            print("ERROR: {} doesn't exist".format(path))
            return (None)

    def display(self, array):
        try:
            img = Image.fromarray(array)
            img.show()
        except Exception:
            print("ERROR: can't display")


img = ImageProcessor()
data = img.load("image/screen.png")
img.display(data)
