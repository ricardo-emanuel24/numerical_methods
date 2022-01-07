import newton_raphson 
import numpy as np
import newton_raphson2

def f(x):
    return np.cosh(x)*np.cos(x) - 1

def df(x):
    return np.sin(x)*np.cos(x) - np.cosh(x)*np.sin(x)

print(newton_raphson.newtonRaphson(f,df,4.0,5.0))

print(newton_raphson2.newtonRaphson(f,df,3.5))