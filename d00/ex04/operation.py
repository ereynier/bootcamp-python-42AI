import sys

if (len(sys.argv) != 3):
    sys.exit("Two numbers needed")
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
except ValueError:
    sys.exit("Numbers needed")
if (a.is_integer()):
    a = int(a)
if (b.is_integer()):
    b = int(b)

print("Sum:         ", a + b)
print("Difference:  ", a - b)
print("Product:     ", a * b)
if (b == 0):
    print("Quotient:     ERROR (div by zero)")
    print("Remainder:    ERROR (modulo by zero)")
else:
    print("Quotient:    ", a / b)
    print("Remainder:   ", a % b)
