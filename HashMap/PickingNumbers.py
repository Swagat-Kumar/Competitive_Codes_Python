#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    dic = {}
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    maxLen = -1
    for d in dic:
        if d-1 not in dic:
            if dic[d] > maxLen:
                maxLen = dic[d]
            continue
        if dic[d-1]+dic[d] > maxLen:
            maxLen = dic[d]+dic[d-1]
    return maxLen


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
