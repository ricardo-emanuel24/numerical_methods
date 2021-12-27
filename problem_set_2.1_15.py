import numpy as np
from LUdecomp import *
from numpy.linalg import inv
from math import *

#----------------------15--------------------- Hilbert matrix

n = 7
A = np.zeros([n,n])
b = np.zeros(n)
for i in range(n):
    for j in range(n):
        A[i, j] = 1/(i+j+1)
        b[i] += A[i,j]

A = LUdecomp(A)
x = LUsolve(A, b)
#print(A)
print(x)
print()
