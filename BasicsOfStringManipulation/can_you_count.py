t = int(input())
ans = []
for i in range(t):
    st = input()
    num = 1
    vList = []
    for s in st:
        if s in ('a', 'e', 'i', 'o', 'u'):
            if s not in vList:
                vList.append(s)
            continue
        if s == '_':
            num *= len(vList)
    ans.append(num)

for a in ans:
    print(a)
