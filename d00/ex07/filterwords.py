import sys

if (len(sys.argv) != 3):
    sys.exit("ERROR")
try:
    n = int(sys.argv[2])
except ValueError:
    sys.exit("ERROR")
try:
    int(sys.argv[1])
    sys.exit("ERROR")
except ValueError:
    s = sys.argv[1]

sp = "".join((char if char.isalpha() else " ") for char in s).split()

for i in range(len(sp) - 1, - 1, - 1):
    if len(sp[i]) <= n:
        del sp[i]
print(sp)
