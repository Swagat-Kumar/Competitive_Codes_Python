#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.


def equalizeArray(arr):
    dic = {}
    c = 0
    for a in arr:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
        c += 1
    maxx = 0
    for d in dic:
        if dic[d] > maxx:
            maxx = dic[d]
    return c-maxx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
