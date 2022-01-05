import numpy as np
from newton_raphson_System import newtonRaphson

def f(x):
    f = np.zeros(len(x))
    f[0] = x[0]**2 + x[1]**2 - 3
    f[1] = x[0]*x[1] - 1
    return f

x = np.array([0.5,1.5])
print()
print(newtonRaphson(f,x))