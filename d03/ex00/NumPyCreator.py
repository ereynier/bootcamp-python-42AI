import numpy as np


class NumPyCreator():
    def __init__(self):
        pass

    def from_list(self, lst):
        if isinstance(lst, list):
            return (np.asarray(lst))
        else:
            return (None)

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple):
            return (np.asarray(tpl))
        else:
            return (None)

    def from_iterable(self, itr):
        try:
            iter(itr)
            return(np.asarray(itr))
        except Exception:
            return (None)

    def from_shape(self, shape, value=0):
        if isinstance(shape, tuple):
            a = np.zeros(shape, dtype=type(value))
            a.fill(value)
            return (a)
        else:
            return (None)

    def random(self, shape):
        if isinstance(shape, tuple):
            return(np.random.random_sample(shape))
        else:
            return (None)

    def identity(self, n):
        if isinstance(n, int):
            return (np.identity(n))
        else:
            return (None)
