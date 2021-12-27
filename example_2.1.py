from math import *
from numpy import array 

def determinante_matrix2x2(m):
    return (m[0][0]*m[1][1] - m[0][1]*m[1][0])

#---------------------------------------SLICES----------------------------------

def determinante_3x3(A):
    det1 = determinante_matrix2x2(A[1:, 1:])
    det2 = determinante_matrix2x2(A[1:, [0, 2]])
    det3 = determinante_matrix2x2(A[1:,:2])
    return A[0,0]*det1 - A[0,1]*det2 + A[0,2]*det3

#-------------------------------------------------------------------------

matrix = array([[2.1, -0.6, 1.1], [3.2, 4.7, -0.8], [3.1, -6.5, 4.1]])
len = len(matrix)

print(matrix, '\n')

determinante = 0
for column in range(len):
    matrix1 = []
    for row in range(1, len):
        matrix2 = []

        for i in range(len):
            if i != column:
                matrix2.append(float(matrix[row][i]))

        matrix1.append(matrix2)

    det_2x2 = determinante_matrix2x2(matrix1)

    determinante += ((-1)**(column%2)*det_2x2*matrix[0][column])

print("%.5f" % determinante)

det = determinante_3x3(matrix)
print("%.5f" % det)