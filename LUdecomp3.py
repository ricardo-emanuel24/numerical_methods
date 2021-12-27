import numpy as np 

def LUdecomp3(c, d, e):
    n = len(d)
    for k in range(n-1):
        lamb = c[k]/d[k]
        d[k+1] = d[k+1] - lamb*e[k]
        c[k] = lamb

    return c, d, e

def LUsolve3(c,d,e,b):
    n = len(d)
    
    for k in range(1,n):
        b[k] = b[k] - c[k-1]*b[k-1]
   
    b[n-1] = b[n-1]/d[n-1]
    for k in range(n-2,-1,-1):
      b[k] = (b[k] - e[k]*b[k+1])/d[k]
    
    return b
    
d = np.ones((5))*2.0
c = np.ones((4))*(-1.0)
b = np.array([5.0, -5.0, 4.0, -5.0, 5.0])
e = c.copy()

c, d, e = LUdecomp3(c,d,e)
x = LUsolve3(c, d, e, b)

print(x)