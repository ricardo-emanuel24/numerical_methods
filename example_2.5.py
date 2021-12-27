from numpy import array
from LUdecomp import *
A = array([[1.0,4.0,1.0],[1.0,6.0,-1.0],[2.0,-1.0,2.0]])
b = array([7.0,13.0,5.0])
a = LUdecomp(A)
x = LUsolve(a, b)
print(x)
