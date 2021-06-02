sumB = -50000000000


def recurr(arr):
    for i in range(len(arr)):
        inrecurr(0, arr, i)


def inrecurr(sumA, arr, current):
    sumA += arr[current]
    for i in range(current+2, len(arr)):
        inrecurr(sumA, arr, i)
    global sumB
    if sumA > sumB:
        sumB = sumA


arr = list(map(int, input().split()))
recurr(arr)
print(sumB)
