#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    amount = 0
    for i in range(0, k):
        amount += bill[i]
    for j in range(k+1, len(bill)):
        amount += bill[j]
    if amount//2 == b:
        print('Bon Appetit')
    else:
        print(b-amount//2)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
