import numpy as np
import galois


GF = galois.GF (9)

A = GF([[6, 7, 5, 7, 1], [4, 4, 6, 1, 0], [6, 7, 2, 6, 5], [8, 5, 7, 6, 7], [6, 8, 2, 7, 6]])
b = GF([6, 2, 7, 6, 1])
x = np.linalg.solve(A, b)
print(x)
#[6, 2, 7, 6, 1]
#[2, 8, 6, 6, 6]