import numpy as np
from LUpivoting import *

def inverts(A):
    n = len(A)
    I = np.identity(n)
    a, seq = LUdecomp(A)

    for i in range(n):
        I[:,i] = LUsolve(a,I[:,i],seq)
    
    return I

def new_func(n):
    x = np.zeros((n,n))

A = np.array([[ 0.6,-0.4, 1.0],\
              [-0.3, 0.2, 0.5],\
              [ 0.6,-1.0, 0.5]])

B= np.array([[0,1,3],[3,-1,2],[-2,2,-4]]).astype(float)

print(inverts(B))
