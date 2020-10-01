t = int(input())
for tt in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    ai.sort()
    s = 0
    j = len(ai)-1
    maxE = ai[j]+1
    for i in range(len(ai)):
        if i % 2 == 0:
            ai[i] += (ai[j] % maxE)*maxE
            j -= 1
        else:
            ai[i] += (ai[s] % maxE)*maxE
            s += 1
    for i in range(len(ai)):
        ai[i] //= maxE
    for a in ai:
        print(a, end=' ')
    print()
