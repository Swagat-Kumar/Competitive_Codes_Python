t = int(input())
for tt in range(t):
    m, n = map(int, input().split())
    ai = list(map(int, input().split()))
    k = 0
    r, c = 0, 0
    depth = 0
    add = 1
    hori = True
    while k < len(ai):
        print(ai[m*r+c], end=' ')
        if hori:
            if c == depth and r == m-1-depth:
                add = -1
                hori = False
            elif c == n-1-depth and r == depth:
                add = 1
                hori = False
        else:
            if r == m-1-depth and c == n-1-depth:
                add = -1
                hori = True
            elif r == depth+1 and c == depth:
                add = 1
                hori = True
                depth += 1
        if hori:
            c += add
        else:
            r += add
        k += 1
    print()
