#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.


def birthday(s, d, m):
    if len(s) < m:
        print(0)
    else:
        count = 0
        initialSum = 0
        for i in range(m):
            initialSum += s[i]
        if initialSum == d:
            count += 1
        i = 0
        for j in range(m, len(s)):
            initialSum -= s[i]
            i += 1
            initialSum += s[j]
            if initialSum == d:
                count += 1
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
