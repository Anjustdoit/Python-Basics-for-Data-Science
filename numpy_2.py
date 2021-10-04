import numpy as np
a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
print(b.ndim)
print(b.shape)
print(a[0][0:2])

Y = np.array([[2, 1], [1, 2]]) 
X = np.array([[1, 0], [0, 1]]) 
Z = X*Y
print(Z)

A = np.array([[0, 1, 1], [1, 0, 1]])
A
B = np.array([[1, 1], [1, 1], [-1, 1]])
B


Z = np.dot(A,B)
print(Z)

np.sin(Z)

C = np.array([[1,1],[2,2],[3,3]])
C

print(C.T)