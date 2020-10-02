import numpy as np
n, m = map(int, input().split())
matrix = []
matrix.append([0]*m)
for i in range(n):
    matrix.append(list(map(int, input().split())))
matrix.append([0]*m)
maxG = -1
for j in range(1, m):
    for i in range(1, n+1):
        matrix[i][j] = matrix[i][j] + \
            max(matrix[i+1][j-1], matrix[i-1][j-1], matrix[i][j-1])
        maxG = max(maxG, matrix[i][j])
print(np.matrix(matrix))
print(maxG)
