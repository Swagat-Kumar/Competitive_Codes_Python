#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return 1+utopianTree(n-1)
    else:
        return 2*utopianTree(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
