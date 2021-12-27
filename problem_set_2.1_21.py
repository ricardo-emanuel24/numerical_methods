import numpy as np
from LUdecomp import *
from numpy.linalg import inv
from math import *

#---------------------21---------------------- Condition Number

def euclidean_norm(A):
    return np.sqrt(np.sum(A**2))

def row_sum_norm(A):
    return np.max(np.sum(np.abs(A), axis = 1)) #Axis = 1 para linhas; Axis = 0 para colunas

A = np.array([[1.0, -1.0, -1.0], [0.0, 1.0, -2.0],[0.0, 0.0, 1.0]]).astype(float)
Ainv = inv(A)
number_condition1 = euclidean_norm(A)*euclidean_norm(Ainv)
number_condition2 = row_sum_norm(A)*row_sum_norm(Ainv)

print("Condition number based on euclidean norm: %f" %number_condition1)
print()
print("Condition number based on row-sum norm: %f" %number_condition2)