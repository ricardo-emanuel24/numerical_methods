import numpy as np
import math

def conjGrad(Ax, x,b,tol=1.0e-9):
    n = len(b)
    r = b - Ax(x)
    s = r.copy()
    
    for i in range(n):
        u = Ax(s)
        alpha = np.dot(s,r)/np.dot(s,u)
        x = x + alpha*s
        r = b - Ax(x)
    
        if(math.sqrt(np.dot(r,r))) < tol:
            break
        
        else:
            beta = -np.dot(r,u)/np.dot(s,u)
            s = r + beta*s
        
    return x,i

def Av(v):
    n = len(v)
    Ax = np.zeros(n)
    Ax[0] = 2.0*v[0] - v[1]+v[n-1]
    Ax[1:n-1] = -v[0:n-2] + 2.0*v[1:n-1] -v[2:n]
    Ax[n-1] = -v[n-2] + 2.0*v[n-1] + v[0]
    return Ax

n = 20
b = np.zeros(n)
b[n-1] = 1.0
x = np.zeros(n)
x,numIter = conjGrad(Av,x,b)
print(x)

