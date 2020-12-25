t = int(input())
ans = []
for i in range(t):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    ai.sort()
    maxSum = sum(ai[len(ai)-(n-m):len(ai)])
    minSum = sum(ai[0:n-m])
    ans.append(maxSum-minSum)
for a in ans:
    print(a)
