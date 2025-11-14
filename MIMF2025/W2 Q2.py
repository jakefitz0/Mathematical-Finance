#Problem 2: Build a function which checks if two matrices can be multiplied and then multiplies them.
# conditions: Gaussian Elimination --> 
    # [ Swap any two rows
    # [ Multiply any row by a scalar]
    # [ add/subtract any 2 rows]

import numpy as np

#initialize matrices
A = np.array ( [ [3,2], [-1,0], [3,3] ] )
B = np.array ( [ [3,2], [-1,0], ] )
 
#can we mult. matrices?
def canMult(A,B):
    if np.shape(A)[1] == np.shape(B)[0]:
        return True
    else:
        return False
#multiply matrices
def mult(A,B):
    if canMult(A,B):
        return np.dot(A,B)
    else:
        return "Matrices cannot be multiplied"
print(mult(A,B))

    


