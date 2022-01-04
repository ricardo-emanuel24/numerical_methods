from newton_raphson import newtonRaphson

def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752
def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538

print(newtonRaphson(f,df,2.2,3.0))