import numpy as np
import desenfoque as des
import jacobi as jac
import gauss as gau

A = np.random.rand(3, 3)
print(f"A = \n{A}")
print(len(A), ",", len(A[0]))
x = des.igual(A)
d = des.desenfoque(A)
print(f"d = \n{d}")
print(len(d), ",", len(d[0]))

x0 = np.zeros_like(x)

#j = jac.jacobi(d, x, x0, n=10)
#g = gau.gauss(d)
