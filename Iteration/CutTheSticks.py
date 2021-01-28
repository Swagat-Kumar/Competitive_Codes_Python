#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):
    ans = [len(arr)]
    aux = list(arr)
    while len(aux) != 0:
        minn = min(aux)
        temp = []
        for a in aux:
            if a == minn:
                continue
            else:
                temp.append(a-minn)
        if len(temp) == 0:
            break
        ans.append(len(temp))
        aux = list(temp)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
