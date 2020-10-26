import bisect
N = int(input())
Ai_array = list(map(int, input().split()))
Ai_array.sort()
Q = int(input())
ans = []
for i in range(Q):
    M = int(input())
    ans.append(bisect.bisect_left(Ai_array, M))
for i in ans:
    print(i)
