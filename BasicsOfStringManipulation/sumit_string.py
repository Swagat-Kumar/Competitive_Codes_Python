t = int(input())
ans = []


def distance(x, y):
    return min(abs(ord(x)-ord(y)), 26-abs(ord(x)-ord(y)))


for i in range(t):
    st = input()
    s = "YES"
    for j in range(len(st)-1):
        if distance(st[j], st[j+1]) != 1:
            s = "NO"
            break
    ans.append(s)
for a in ans:
    print(a)
