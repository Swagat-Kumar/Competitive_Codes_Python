t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = list(arr)
    s = []
    for i in range(len(arr)-1, -1, -1):
        while len(s) > 0 and arr[i] >= s[-1]:
            s.pop()
        if len(s) == 0:
            ans[i] = -1
        else:
            ans[i] = s[-1]
        s.append(arr[i])
    for a in ans:
        print(a, end=' ')
    print()
