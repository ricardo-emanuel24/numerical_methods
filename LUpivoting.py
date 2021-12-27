import numpy as np

def LUdecomp(a):
    n = len(a)
    seq = np.array(range(n))

    s = np.zeros((n))
    for i in range(n):
        s[i] = max(abs(a[i,:]))

    for k in range(0,n-1):
    # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if p != k:
            swap(s,k,p)
            swap(a,k,p)
            swap(seq,k,p)  

    # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
    return a,seq

def LUsolve(a,b,seq):
    n = len(a)

    # Rearrange constant vector; store it in [x]
    x = b.copy()
    for i in range(n):
        x[i] = b[seq[i]]
    
    # Solution
    for k in range(1,n):
        x[k] = x[k] - np.dot(a[k,0:k],x[0:k])
    x[n-1] = x[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (x[k] - np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    return x

def swap(v,k,p):
    v[[k,p]]=v[[p,k]]
    return v

'''
A=np.array([[2,-2,6],[-2,4,3],[-1,8,4]]).astype(float)
b=np.array([16,0,-1]).astype(float)

a, seq=LUdecomp(A)
x=LUsolve(A,b,seq)
print(x)'''