t = int(input())
for i in range(t):
    line = input()
    line = sorted(line)
    x = line[0]
    distinct = 0
    ans = 1
    for s in line:
        if s == x:
            distinct += 1
        else:
            x = s
            if distinct != 0:
                ans *= (distinct)
            distinct = 1
    if distinct != 0:
        ans *= (distinct)
    print(ans % (10**9+7))
