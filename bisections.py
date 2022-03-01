import math
from numpy import sign

def bisection(f,x1,x2,tol,switch):

    n = math.ceil(math.log(abs(x2-x1)/tol)/math.log(2))
    
    f1 = f(x1)
    f2 = f(x2)

    for i in range(n):
        x3 = (x2+x1)/2
        f3 = f(x3)
        
        if (switch == 1) and (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
            return None

        if sign(f1) != sign(f3):
            x2 = x3
            f2 = f3
            
        elif sign(f2) != sign(f3):
            x1 = x3
            f1 = f3
        
        else:
            return None

    return (x2+x1)/2

def f(x): return x**3 - 10.0*x**2 + 5.0

x1, x2 = 0.0, 1.0
tol=1.0e-4
switch=1
root = bisection(f, x1, x2, tol, switch)

print(root)
