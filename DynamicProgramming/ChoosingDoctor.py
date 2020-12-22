t = int(input())


def score(arr):
    if len(arr) <= 2:
        return max(arr)
    aux = [0]*len(arr)
    aux[0] = arr[0]
    aux[1] = max(aux[0], arr[1])
    maxx = aux[1]
    for i in range(2, len(arr)):
        aux[i] = max(aux[i-1], arr[i]+aux[i-2])
        if aux[i] > maxx:
            maxx = aux[i]
    return maxx


for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    print('Case '+str(i+1)+': '+str(score(ar)))
