import glob
import os

t = (0, 4, 132.42222, 10000, 12345.67)

s = ""

os.chdir("../../")
for folder in glob.glob("*{0:02d}".format(*t)):
    s += "{}, ".format(folder)
os.chdir("{}/".format(folder))

for folder in glob.glob("*{1:02d}".format(*t)):
    s += "{} : ".format(folder)

for i in range(2, len(t)):
    s += "{:.2e}".format(t[i])
    if (i < len(t) - 1):
        s += ", "
print(s)
