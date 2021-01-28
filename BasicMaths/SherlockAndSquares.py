#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.


def squares(a, b):
    aRoot = math.floor(a**0.5)
    bRoot = math.floor(b**0.5)
    ans = 0
    if aRoot*aRoot == a:
        ans += 1
    ans += bRoot-aRoot
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
