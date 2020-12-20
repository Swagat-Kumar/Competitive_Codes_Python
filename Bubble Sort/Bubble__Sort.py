n = int(input())
ai = list(map(int, input().split()))


def bubblesort(a):
    count = 0
    n = len(a)
    swapped = True
    while swapped != False:
        swapped = False
        count += 1
        for i in range(1, n-1):
            if (a[i] > a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                swapped = True
    return count


print(bubblesort(ai))
