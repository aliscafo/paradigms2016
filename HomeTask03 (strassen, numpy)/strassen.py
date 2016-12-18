import numpy
from math import ceil, log


def printMatrix(matrix):
    for line in matrix:
        print(" ".join(map(str,line)))
        
        
def strassen(A, B):
    n = len(A)
    if n == 1:
        return A * B

    newSize = n // 2
    A11 = A[:newSize, :newSize]
    A12 = A[:newSize, newSize:]
    A21 = A[newSize:, :newSize]
    A22 = A[newSize:, newSize:]
    
    B11 = B[:newSize, :newSize]
    B12 = B[:newSize, newSize:]
    B21 = B[newSize:, :newSize]
    B22 = B[newSize:, newSize:]
    
    M1 = strassen(A12 - A22, B21 + B22)
    M2 = strassen(A11 + A22, B11 + B22)
    M3 = strassen(A11 - A21, B11 + B12)
    M4 = strassen(A11 + A12, B22)
    M5 = strassen(A11, B12 - B22)
    M6 = strassen(A22, B21 - B11)
    M7 = strassen(A21 + A22, B11)
    
    C11 = M1 + M2 - M4 + M6
    C12 = M4 + M5
    C21 = M6 + M7
    C22 = M2 - M3 + M5 - M7
    
    return numpy.vstack((numpy.hstack((C11, C12)), numpy.hstack((C21, C22))))
            

if __name__ == '__main__':
    n = int(input())
    n_power2 = 2 ** int(ceil(log(n, 2)))
    
    A = numpy.zeros((n_power2, n_power2), dtype=numpy.int)
    B = numpy.zeros((n_power2, n_power2), dtype=numpy.int)
         
    k = []
    for i in range(n):
        k.append([int(x) for x in input().split()])
    A[:n, :n] = numpy.matrix(k) 

    q = []
    for i in range(n):
        q.append([int(x) for x in input().split()])
    B[:n, :n] = numpy.matrix(q) 
    
    RES = strassen(A, B)  
    printMatrix(RES[:n, :n])
    