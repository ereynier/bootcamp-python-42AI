from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

img = ImageProcessor()
col = ColorFilter()
data = img.load("image/screen.png")
data1 = col.invert(data)
data2 = col.to_blue(data)
data3 = col.to_green(data)
data4 = col.to_red(data)
data5 = col.celluloid(data, 11)
img.display(data)
img.display(data1)
img.display(data2)
img.display(data3)
img.display(data4)
img.display(data5)
