import numpy as np


class ColorFilter():
    def __init__(self):
        pass

    def invert(self, array):
        return (255 - array)

    def to_blue(self, array):
        arr = np.zeros(np.shape(array), dtype=np.uint8)
        arr[0:, 0:, 2:] = array[0:, 0:, 2:]
        return(arr)

    def to_green(self, array):
        return (array * np.uint8([0, 1, 0]))

    def to_red(self, array):
        return (array - self.to_green(array) - self.to_blue(array))

    def celluloid(self, array, num=5):
        sp = np.linspace(0, 255, num)
        sp = np.uint8(sp)
        return (array - array % int(sp[1]))
        # return (array * 0 + sp[int(64/255 * 4)])
