t = int(input())
for tt in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    if ai[0] != ai[1]:
        print(ai[0])
    elif ai[-1] != ai[-2]:
        print(ai[-1])
    else:
        low = 1
        high = len(ai)-2
        while low <= high:
            mid = (low+high)//2
            if ai[mid] != ai[mid-1] and ai[mid] != ai[mid+1]:
                print(ai[mid])
                break
            if (mid % 2 != 0 and ai[mid] == ai[mid+1]) or (ai[mid] == ai[mid-1] and mid % 2 == 0):
                high = mid-1
            else:
                low = mid+1
