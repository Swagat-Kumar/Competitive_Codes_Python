n = int(input())
ai = list(map(int, input().split()))
lowSum = ai[0]
highSum = ai[len(ai)-1]
low = 0
high = len(ai) - 1
while low < high:
    if lowSum == highSum:
        low += 1
        high -= 1
        highSum += ai[high]
        lowSum += ai[low]
        continue
    if lowSum < highSum:
        low += 1
        lowSum += ai[low]
    else:
        high -= 1
        highSum += ai[high]
if highSum == lowSum:
    if ((low+high)/2) == ((low+high)//2):
        print((low+high)/2)
    else:
        print(-1)
else:
    print(-1)
