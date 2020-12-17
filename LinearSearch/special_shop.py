import math
T = int(input())
Ans = []
for i in range(T):
    Line_Array = list(map(int, input().split()))
    N = Line_Array[0]
    A = Line_Array[1]
    B = Line_Array[2]
    x = math.floor((B*N)/(A+B))
    xx = math.ceil((B*N)/(A+B))
    cost = A*(x**2)+B*((N-x)**2)
    costx = A*(xx**2)+B*((N-xx)**2)
    Ans.append(min(costx, cost))
for k in Ans:
    print(k)
