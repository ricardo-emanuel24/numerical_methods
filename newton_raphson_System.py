import numpy as np
from gauss_pivoting import *
import math

def jacobian(f,x):
    h = 1.0e-4
    n = len(x)
    J = np.zeros((n,n))
    f0 = f(x)
    t = np.zeros(n)

    for i in range(n):
        x[i] = x[i] + h
        f1 = f(x)
        x[i] = x[i] - h
        J[:,i] = (f1 - f0)/h
        print((f1 - f0)/h)
    return J,f0
    


def newtonRaphson(f,x,tol=1.0e-9):
    n = len(x)
    dx = np.ones(n)

    while math.sqrt(np.dot(dx,dx)) > tol*max(max(abs(x)),1.0):
        jac,f0 = jacobian(f,x)

        if math.sqrt(np.dot(f0,f0)/len(x)) < tol:
             return x

        dx = gauss_pivoting(jac,-f0)
        x = x + dx

    return x

