from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor

img = ImageProcessor()
scrap = ScrapBooker()
data = img.load("image/screen.png")
# data = scrap.crop(data, (800, 1200), (200,200))
# data = scrap.thin(data, 2, 0)
# data = scrap.juxtapose(data, 2, 1)
data = scrap.mosaic(data, (3, 2))
print(len(data[0]), len(data))
img.display(data)
