#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    maxx = scores[0]
    minn = scores[0]
    mincount = 0
    maxcount = 0
    for i in range(1, len(scores)):
        if scores[i] < minn:
            minn = scores[i]
            mincount += 1
        if scores[i] > maxx:
            maxx = scores[i]
            maxcount += 1
    return [maxcount, mincount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
