#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.


def bigSorting(unsorted):
    def less(a, b):
        aLength = len(a)
        bLength = len(b)
        if (aLength != bLength):
            if aLength > bLength:
                return 1
            return -1
        for i in range(aLength):
            if a[i] == b[i]:
                continue
            if a[i] > b[i]:
                return 1
            else:
                return -1
        return 0

    def sort(a, lo, hi):
        if lo >= hi:
            return
        v = a[lo]
        i = lo
        lt = lo
        gt = hi
        while i <= gt:
            cmp = less(a[i], v)
            if cmp < 0:
                a[lt], a[i] = a[i], a[lt]
                i += 1
                lt += 1
            elif cmp > 0:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        sort(a, lo, lt-1)
        sort(a, gt+1, hi)
    sort(unsorted, 0, len(unsorted)-1)
    return unsorted


    # Merge Sort
    # def merge(a,aux,low,mid,hi):
    #     for i in range(low,hi+1):
    #         aux[i]=a[i]
    #     i=low
    #     j=mid+1
    #     k=low
    #     while k<=hi:
    #         if i>mid:
    #             a[k]=aux[j]
    #             j+=1
    #         elif j>hi:
    #             a[k]=aux[i]
    #             i+=1
    #         elif less(aux[i],aux[j]):
    #             a[k]=aux[i]
    #             i+=1
    #         else:
    #             a[k]=aux[j]
    #             j+=1
    #         k+=1
    # def sort(a,aux,lo,hi):
    #     if lo>=hi:
    #         return
    #     mid=(lo+hi)//2
    #     sort(a,aux,lo,mid)
    #     sort(a,aux,mid+1,hi)
    #     merge(a,aux,lo,mid,hi)
    # b=[0]*len(unsorted)
    # sort(unsorted,b,0,len(b)-1)
    # return unsorted
    # Shell Sort
    # h=1
    # while h<len(unsorted)//3:
    #     h=3*h+1
    # while h>=1:
    #     for i in range(h,len(unsorted)):
    #         for j in range(i,h-1,-h):
    #             if less(unsorted[j],unsorted[j-h]):
    #                 unsorted[j],unsorted[j-h]=unsorted[j-h],unsorted[j]
    #             else:
    #                 break
    #     h=h//3
    # return unsorted
    # Insertion Sort
    # for i in range(len(unsorted)):
    #     minn=i
    #     for j in range(i,len(unsorted)):
    #         if less(unsorted[j],unsorted[minn]):
    #             minn=j
    #     unsorted[i],unsorted[minn]=unsorted[minn],unsorted[i]
    # return unsorted
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
