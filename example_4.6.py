from newton_raphson import newtonRaphson

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

print(newtonRaphson(f,df,1.4,2.0))