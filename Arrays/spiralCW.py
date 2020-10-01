import numpy as np
t = int(input())
for tt in range(t):
    n = int(input())
    arr = [[-1]*n for i in range(n)]
    i = 1
    left = 0
    right = n-1
    top = 0
    bottom = n-1
    while i <= n*n:
        for j in range(left, right+1):
            arr[top][j] = i
            i += 1
        top += 1
        for j in range(top, bottom+1):
            arr[j][right] = i
            i += 1
        right -= 1
        for j in range(right, left-1, -1):
            arr[bottom][j] = i
            i += 1
        bottom -= 1
        for j in range(bottom, top-1, -1):
            arr[j][left] = i
            i += 1
        left += 1
    print(np.matrix(arr))
