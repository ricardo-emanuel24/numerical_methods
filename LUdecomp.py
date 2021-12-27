import numpy as np

def LUdecomp(a):
    n = len(a)
# Decomposition Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                Lambda = float(a[i,k]/a[k,k])
                a[i,k:n] = a[i,k:n] - Lambda*a[k,k:n]
                a[i, k] = float(Lambda)
    return a
def LUsolve(a, b):
# Solution phase
    n=len(b)
    for k in range(1,n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
    
