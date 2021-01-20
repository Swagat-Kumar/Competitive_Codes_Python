#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.


def formingMagicSquare(s):
    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    minCost = 10**7

    def checkCost(s, p):
        cost = 0
        for r in range(3):
            for c in range(3):
                cost += abs(s[r][c]-p[r][c])
        return cost
    for p in pre:
        cost = checkCost(s, p)
        if cost < minCost:
            minCost = cost
    return minCost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

# def isMagicSquare(ar):
#     n = len(ar)
#     summ = (n*(n**2+1))//2
#     for a in ar:
#         if sum(a) != summ:
#             return False
#     for c in range(n):
#         aux = 0
#         for r in range(n):
#             aux += ar[r][c]
#         if aux != summ:
#             return False
#     ltr = 0
#     rtl = 0
#     for i in range(n):
#         ltr += ar[i][i]
#         rtl += ar[n-1-i][n-1-i]
#     if ltr != summ or rtl != summ:
#         return False
#     return True


# print(isMagicSquare([[8, 1, 6], [3, 5, 7], [4, 9, 6]]))
