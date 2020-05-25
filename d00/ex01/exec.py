import sys

n = len(sys.argv) - 1
out = ""

for i in range(n, 0, -1):
    for j in range(len(sys.argv[i]) - 1, -1, -1):
        out += (sys.argv[i][j])
    if (i != 1):
        out += " "
print(out.swapcase())
