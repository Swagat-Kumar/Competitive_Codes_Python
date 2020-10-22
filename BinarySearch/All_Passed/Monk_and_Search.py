import bisect
N = int(input())
Ai_array = list(map(int, input().split()))
Ai_array.sort()
Q = int(input())
ans = []
for i in range(Q):
    op, x = map(int, input().split())
    if(op == 0):
        ans.append(N-bisect.bisect_left(Ai_array, x))
    elif(op == 1):
        ans.append(N-bisect.bisect_right(Ai_array, x))
for i in ans:
    print(i)
