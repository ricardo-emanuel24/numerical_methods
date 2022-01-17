import numpy as np
import math

def choleski(A):
    l = len(A)
    L = np.zeros((l, l))
    for j in range(l):
        L[j,j] = math.sqrt(A[j,j]-np.dot(L[j, :j],L[j, :j]))
        for i in range(j+1, l):
            L[i, j] = (A[i, j] - np.dot(L[i, :j], L[j, :j]))/L[j, j]
    return L

#--------------------example2.6-----------------------
A=np.array([[4, -2, 2],[-2, 2, -4],[2, -4, 11]])
L = choleski(A)
print(L)
