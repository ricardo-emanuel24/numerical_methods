from gaussElimin import *
from math import *

def vandermode(v):
    n = len(v)
    A = [0]

    for k in range(n):
        A[k] = [0]*n
        if len(A) != len(v):
            A.append([])

    for i in range(n):
        for j in range(n):
            A[i][j] = (v[i]**(n-j-1))
    return A

v = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
a = np.array(vandermode(v))
b = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
for m in range(len(a)):
    print(a[m])

x = gaussElimin(a, b)

print(x)