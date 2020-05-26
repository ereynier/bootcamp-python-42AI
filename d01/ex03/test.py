from matrix import Matrix
from vector import Vector

m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
m2 = Matrix([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])

v = m1 * m2

print(v)
