from numpy import sign

def searchingroot(f,x1,x2,dx):
    while x1<x2:
        f1=f(x1)
        f2=f(x1+dx)
        if sign(f1) != sign(f2):
            return x1, (x1+dx)
        x1 = x1 + dx


def searchingroot2(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while sign(f1) == sign(f2):
        if x1 >= b: return None,None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)

    return x1,x2

def f(x): return x**3 - 10.0*x**2 + 5.0

x1 = 0.0; x2 = 1.0
for i in range(4):
    dx = (x2 - x1)/10.0
    x1,x2 = searchingroot2(f,x1,x2,dx)

x = (x1 + x2)/2.0
print('x =', '{:6.4f}'.format(x))