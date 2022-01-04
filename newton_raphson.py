from numpy import sign


def newtonRaphson(f,df,a,b,tol=1.0e-9):
    if a > b: return None

    fa = f(a)
    fb = f(b)

    if abs(fa) < tol: return a
    if abs(fb) < tol: return b
    
    if sign(fa) == sign(fb): return None

    x = (a+b)/2
    dx = b - a

    while abs(dx) > tol*max(abs(b),1.0):
        fx = f(x)

        if abs(fx) < tol: return x

        if sign(fa) == sign(fx):
            a = x
        else:
            b = x 

        dfx = df(x)
        if dfx != 0.0:
            dx = - fx/dfx
        else:
            dx = b - a

        x = x + dx

        if x > b or x < a:
            dx = (b-a)/2
            x = a + dx

    return x

