from bisections import bisection
from rootsearch import searchingroot
import math

def f(x): return x - math.tan(x)

a, b, dx = 0.0, 20.0, 0.01

while True:
    x1, x2 = searchingroot(f, a, b, dx)
    if x1 != None and x2 != None:
        a = x2
        root = bisection(f, x1, x2, 1.0e-9, 1)
        if root != None:
            print('{:6.4f}'.format(root))
        else:
            print('Pole between the points:','{:6.4f},{:6.4f}'.format(x1,x2))
    else:
        break
        