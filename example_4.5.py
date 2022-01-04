from ridder import ridder

def f(x):
    a = (x - 0.3)**2 + 0.01
    b = (x - 0.8)**2 + 0.04
    return 1.0/a - 1.0/b

print("root =",ridder(f,0.0,1.0,tol=1.0e-9))