#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.


def beautifulTriplets(d, arr):
    dic = {}
    for a in arr:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    count = 0
    for i in range(len(arr)-1):
        if arr[i]-d in dic and arr[i]+d in dic:
            count += dic[arr[i]-d]*dic[arr[i]+d]
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
