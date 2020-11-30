import math
T = int(input())
ans = []
for i in range(T):
    line_array = list(map(int, input().split()))
    N = line_array[0]
    K = line_array[1]
    P = line_array[2]
    Ai = list(map(int, input().split()))
    Ai.sort()
    c = 0
    k = 1
    while(c <= P):
        if (k == N+1):
            ans.append(-1)
            break
        low = 0
        high = len(Ai)-1
        ans_1 = 0
        while(low <= high):
            mid = math.floor((low+high)/2)
            if(Ai[mid] < k):
                low = mid+1
            elif(Ai[mid] > k):
                high = mid-1
            else:
                ans_1 = 1
                del Ai[mid]
                break
        if(not ans_1):
            c += 1
        if(c == P):
            ans.append(k)
            break
        k += 1
for k in ans:
    print(k)
