import math
T = int(input())
ans_array = []
for i in range(T):
    Data_Numbers = list(map(int, input().split()))
    D = Data_Numbers[0]
    A = Data_Numbers[1]
    M = Data_Numbers[2]
    B = Data_Numbers[3]
    X = Data_Numbers[4]-D
    rate = A*M+B
    months = (M+1)*(math.floor(X/rate))
    remainder = X % rate
    pos = 0
    if(remainder > (A*M)):
        months += M+1
    if(remainder <= (A*M) and remainder != 0):
        low = 1
        high = M
        while(low <= high):
            if(((pos*A)-remainder) < A and ((pos*A)-remainder) >= 0):
                break
            mid = math.floor((low+high)/2)
            if(mid*A < remainder):
                low = mid+1
                pos = mid
            elif(mid*A > remainder):
                high = mid-1
                pos = mid
            else:
                pos = mid
                break
    months += pos
    ans_array.append(months)
for i in ans_array:
    print(i)
