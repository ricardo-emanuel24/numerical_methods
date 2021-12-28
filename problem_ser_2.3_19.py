import numpy as np
from conjGrad import conjGrad

def Av(v):
    n = len(v)
    Ax = np.zeros(n)
    for i in range(n):
        Ax[i] += (-4*v[i])
        if i<6:
            Ax[i] += v[i]
        if i>2:
            Ax[i] += v[i]
        if i != 3 or


b=np.array([0,0,100,0,0,100,200,200,300])