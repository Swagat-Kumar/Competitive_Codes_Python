#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.


def designerPdfViewer(h, word):
    count = 0
    maxHeight = 0
    for l in word:
        letterHeight = h[ord(l)-97]
        if letterHeight > maxHeight:
            maxHeight = letterHeight
        count += 1
    return count*maxHeight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
