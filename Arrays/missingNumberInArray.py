# code
t = int(input())
for tt in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    ai.sort()
    if n > 3:
        low = 1
        high = len(ai)-2
        if ai[0] != 1:
            print(1)
        while low <= high:
            mid = (low+high)//2
            if ai[mid] != ai[mid-1]+1:
                print(mid+1)
                break
            if ai[mid] != ai[mid+1]-1:
                print(mid+2)
                break
            if ai[mid] == mid+1:
                low = mid+1
            else:
                high = mid-1
        if ai[-1] != n:
            print(n)
    else:
        for i in range(len(ai)):
            if ai[i] != i+1:
                print(i+1)
                break
        if ai[-1] != n:
            print(n)
