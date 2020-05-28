import numpy as np


class ScrapBooker():
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        if (dimensions[0] + position[0] > len(array) or
                dimensions[1] + position[1] > len(array[1])):
            print("ERROR: new size too big")
            return (array)
        else:
            arr = array[position[0]:dimensions[0] + position[0],
                        position[1]:dimensions[1] + position[1]]
            return (arr)

    def thin(self, array, n, axis):
        nb = n
        arr = array
        if (axis == 1 and n > 1):
            while (n < np.size(arr, 1)):
                arr = np.delete(arr, n, axis)
                n += nb
        elif (axis == 0 and n > 1):
            while (n < np.size(arr, 0)):
                arr = np.delete(arr, n, axis)
                n += nb
        return(arr)

    def juxtapose(self, array, n, axis):
        arr = array
        if (axis == 0):
            for i in range(n):
                arr = np.concatenate((arr, array), 0)
        elif (axis == 1):
            for i in range(n):
                arr = np.concatenate((arr, array), 1)
        return (arr)

    def mosaic(self, array, dimensions):
        arr = array
        for i in range(dimensions[0] - 1):
            arr = np.concatenate((arr, array), 0)
        arr2 = arr
        for i in range(dimensions[1] - 1):
            arr = np.concatenate((arr, arr2), 1)
        return (arr)
