#Problem 3: Build a function which takes A and computes A^T
def trpose(A):
    #get # of rows and colums
    n1 = np.shape(A)[0]
    n2 = np.shape(A)[1]
    #create shape of the transpose
    sh = (n2,n1)
    #initialize an empty matric (zeroes)
    AT = np.zeros(shape=sh)

    for i in range(n2):    #for i in the range of the number of rows in A^T
        for j in range(n1): #for j in range of the number of cols in A^T
            #make the a_ijth entry of A^T the a_jith entry of A
            AT[i][j] = A[j][i]
        return AT
    
    A = np.array ( [ [3,2], [-1,0], [3,3] ] )
    print(trpose(A))



#Problem 4: Build a function which determines if a list of vectors is an orthogonal or orthonormal basis by computing A^T A
# and checking if it is diagonal / I. (Hint: Use your function from problem 3!)

import numpy as np
print(np.__version__)
def is_orthogonal(vectors):
    n = len(vectors)
    for i in range(n):
        for j in range(i + 1, n):
            if ip(vectors[i], vectors[j]) != 0:
                return False
    return True

def is_orthonormal(vectors):
    n = len(vectors)
    for i in range(n):
        if ip(vectors[i], vectors[i]) != 1:
            return False
        for j in range(i + 1, n):
            if ip(vectors[i], vectors[j]) != 0:
                return False
    return True

#put test cases here
v1 = [1,0,0]
v2 = [0,1,0]
v3 = [0,0,1]
vectors = [v1, v2, v3]
print(f'The vectors {vectors} are orthogonal: {is_orthogonal(vectors)}')
print(f'The vectors {vectors} are orthonormal: {is_orthonormal(vectors)}')






