t = int(input())
ans = []
for i in range(t):
    st = input()
    a = ''
    for s in st:
        if s not in a:
            a += s
    ans.append(a)
for a in ans:
    print(a)
