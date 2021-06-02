#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    maxSum = -100
    for r in range(len(arr)-2):
        for c in range(len(arr)-2):
            aux = arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1] + \
                arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2]
            if aux > maxSum:
                maxSum = aux
    return maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
