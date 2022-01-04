from newton_raphson2 import newtonRaphson

def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752
def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538


m = 2.0 # parametro que diminui o número de iterações, é o multiplo da raiz

root, NumIt = newtonRaphson(f,df,2.0,m)
print(root)
print('Numero de Iterações:', NumIt)