#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jumps = [0]*len(c)
    if not c[1]:
        jumps[1] = 1
    for i in range(2, len(c)):
        aux = []
        if not c[i-1]:
            aux.append(jumps[i-1])
        if not c[i-2]:
            aux.append(jumps[i-2])
        if len(aux) != 0:
            jumps[i] = min(aux)+1
        else:
            jumps[i] = 10000
    return jumps[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
