from newton_raphson import newtonRaphson
from rootsearch import searchingroot

def newton_rootsearch(f,df,a,b,dx):
    while True:
        x1, x2 = searchingroot(f, a, b, dx)
        if x1 != None and x2 != None:
            a = x2
            root = newtonRaphson(f,df,x1,x2)

            if root != None:
                print('{:6.4f}'.format(root))

        else:
            break