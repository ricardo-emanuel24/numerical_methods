from numpy import sign

def searchingroot(f,x1,x2,dx):
    f1=f(x1)
    f2=f(x1+dx)

    while sign(f1) == sign(f2):
        if x1 >= x2: return None,None
        x1 = x1 + dx
        f1=f(x1)
        f2=f(x1+dx)

    return x1, (x1+dx)

def f(x): return x**3 - 10.0*x**2 + 5.0

x1 = 0.0; x2 = 1.0
for i in range(4):
    dx = (x2 - x1)/10.0
    x1,x2 = searchingroot(f,x1,x2,dx)
    if x1 == None and x2 == None:
        print('No rooots')
        break

if x1 != None and x2 != None:
    x = (x1 + x2)/2.0
    print('x =', '{:6.4f}'.format(x))
