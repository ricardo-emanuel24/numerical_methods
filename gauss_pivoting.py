import numpy as np

def gauss_pivoting(A,b):
    n = len(A)
    s = np.zeros(n)

    for i in range(n):
        s[i]= max(np.abs(A[i]))

    for k in range(n):
        p = np.argmax(abs(A[k:n,k])/s[k:n])+k
        
        if p != k:
            b=swap(b,k,p)
            A=swap(A,k,p)
            s=swap(s,k,p)
        # Elimination Phase
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                lam = A[i,k]/A[k,k]
                A[i,k:n] = A[i,k:n] - lam*A[k,k:n]
                b[i] = b[i] - lam*b[k]

# Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(A[k,k+1:n],b[k+1:n]))/A[k,k]
    return b

def swap(v,k,p):
    v[[k,p]]=v[[p,k]]
    return v

A=np.array([[2,-2,6],[-2,4,3],[-1,8,4]]).astype(float)
b=np.array([16,0,-1]).astype(float)

x=gauss_pivoting(A,b)
print(x)