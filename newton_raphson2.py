def newtonRaphson(f,df,x,m=1,tol=1.0e-9):
    dx = - f(x)/df(x)
    i=0

    while abs(dx)>tol:
        dx = -m*f(x)/df(x)
        x = x + dx
        i+=1
    
    return x, i