arr = list(map(int, input().split()))
target = int(input())
aux = {}
i = 0
for a in arr:
    compliment = target-a
    if compliment in aux:
        print(a, compliment, ' = ', aux[compliment], i)
    aux[a] = i
    i += 1
