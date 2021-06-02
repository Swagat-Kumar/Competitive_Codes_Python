import numpy as np
marked = [[False]*8 for i in range(8)]


def visited(x, y):
    return marked[x][y]


def allmarked():
    for m in marked:
        for g in m:
            if not g:
                return False
    return True


def solve(x, y):
    for i in range(8):
        for j in range(8):
            if ((x-1 == i and y-2 == j) or (x+1 == i and y+2 == j) or(x-2 == i and y+1 == j) or(x+2 == i and y-1 == j)
                    or (x-2 == i and y-1 == j) or (x+2 == i and y+1 == j) or (x+1 == i and y-2 == j) or (x-1 == i and y+2 == j)):
                if not visited(i, j):
                    marked[i][j] = True
                    solve(i, j)
                    marked[i][j] = False
                    return
    if allmarked():
        print("Can Reach!!")
        print(np.matrix(marked))
        input("Continue.....??")


for x in range(8):
    for y in range(8):
        print(x, y)
        marked = [[False]*8 for i in range(8)]
        marked[x][y] = True
        solve(x, y)
