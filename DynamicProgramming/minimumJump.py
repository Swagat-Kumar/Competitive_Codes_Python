t = int(input())
for tt in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    maxS = None
    re = False

    def recurr(ar):
        print(ar)
        global re
        for i in range(len(ar)-1):
            if i+ar[i] >= len(ar)-1:
                if i == 0:
                    re = True
                    return 1
                else:
                    return 1+recurr(ar[:i+1])
        return 0
    x = recurr(ai)
    if re:
        print(x)
    else:
        print(-1)
