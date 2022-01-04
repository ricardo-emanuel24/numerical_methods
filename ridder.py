import math 
from numpy import sign

def ridder(f,x1,x2,tol):
    f1, f2 = f(x1), f(x2)
    if abs(f1) < tol: return x1
    if abs(f2) < tol: return x2
    xOld = x1

    while True:
        x3 = (x1+x2)/2
        f3 = f(x3)
        s = math.sqrt(f3**2 - f1*f2)

        if s == 0.0: return None

        x4 = x3 + (sign(f1-f2)*(x3-x1)*f3/s)
        f4 = f(x4)
        print(x4)
        if abs(x4 - xOld) < tol*max(abs(x4),1.0): return x4
        xOld = x4
        

        if sign(f3) == sign(f4):
            if sign(f1)!= sign(f4):
                x2 = x4; f2 = f4
            else: 
                x1 = x4; f1 = f4
        
        else:
            x1 = x3; x2 = x4; f1 = f3; f2 = f4