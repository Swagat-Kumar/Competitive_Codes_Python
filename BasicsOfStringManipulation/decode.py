t = int(input())
for i in range(t):
    line = input()
    ans = ''
    c = 0
    if(len(line) % 2 == 1):
        for s in line:
            if c % 2 == 0:
                ans = ans+s
            else:
                ans = s+ans
            c += 1
    else:
        for s in line:
            if c % 2 == 0:
                ans = s+ans
            else:
                ans = ans+s
            c += 1
    print(ans)
