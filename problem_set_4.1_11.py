from newtonRaphson_rootsearch import newton_rootsearch
import numpy as np

def f(x):
    return x*np.sin(x) + 3*np.cos(x) - x

def df(x):
    return (-2*np.sin(x) + x*np.cos(x) - 1)

print(newton_rootsearch(f,df,-6.0,6.0,0.01))