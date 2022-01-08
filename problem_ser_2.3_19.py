import numpy as np
import conjGrad

def Av(T):
    n = len(T)
    Ax = np.zeros(n)
    
    Ax[:] += (4*T[:])
    Ax[:6] -= T[3:]
    Ax[3:] -= T[:6]
    Ax[[0,1,3,4,6,7]] -= T[[1,2,4,5,7,8]]
    Ax[[1,2,4,5,7,8]] -= T[[0,1,3,4,6,7]]

    return Ax

b=np.array([0,0,100,0,0,100,200,200,300]).astype(float)
x = np.zeros(9)

x,numIter = conjGrad.conj_Grad(Av,x,b)

print(x[:3], '\n', x[3:6], '\n', x[6:9])
print(numIter)