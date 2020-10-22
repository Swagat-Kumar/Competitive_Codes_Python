n = int(input())
ai = list(map(int, input().split(" ")))
count = 0

for i in range(n):
    for j in range(n-i-1):
        if ai[j] > ai[j+1]:
            temp = ai[j]
            ai[j] = ai[j+1]
            ai[j+1] = temp
            count += 1
print(count)
