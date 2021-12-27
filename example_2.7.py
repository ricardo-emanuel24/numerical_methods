import numpy as np
from LUdecomp import *
matrixA = np.array([[3.0, -1.0, 4.0], [-2.0, 0.0, 5.0], [7.0, 2.0, -2.0]])
matrixB = np.array([[6.0, 3.0, 7.0], [-4.0, 2.0, -5.0]])

matrixAdecomp = LUdecomp(matrixA)
for i in range(len(matrixB)):
    b = LUsolve(matrixAdecomp,matrixB[i])
    print(b)

det = np.prod(np.diagonal(matrixA)) #Calcula determinantes de qualquer matrix com o numpy
print(det)