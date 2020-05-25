import sys

if (len(sys.argv) != 2):
    sys.exit("1 argument needed")
try:
    i = int(sys.argv[1])
except ValueError:
    sys.exit("integer needed")

if (i == 0):
    print("I'm Zero")
elif (i % 2 == 0):
    print("I'm Even")
else:
    print("I'm Odd")
