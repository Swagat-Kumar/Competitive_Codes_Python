#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.


def permutationEquation(p):
    aux = []
    x = 1
    for c in p:
        aux.append(p.index(p.index(x)+1)+1)
        x += 1
    return aux


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
