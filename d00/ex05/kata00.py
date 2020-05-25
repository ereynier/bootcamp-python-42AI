t = (19, 42, 21)

size = len(t)

s = "The {} numbers are: ".format(size)

for i in range(0, size):
    s += '{}'.format(t[i])
    if (i < size - 1):
        s += ", "
print(s)
