t = int(input())
ans = []


def covert(s):
    if s.isspace():
        return '$'
    else:
        if s.islower():
            return str(ord(s)-96)
        else:
            return str(ord(s)-64)


for i in range(t):
    st = input()
    a = ''
    for s in st:
        a += covert(s)
    ans.append(a)
for a in ans:
    print(a)
