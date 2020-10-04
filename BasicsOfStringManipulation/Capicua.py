t = int(input())
ans = []
for i in range(t):
    s = input()
    reverse = s[::-1]
    if(s == reverse):
        ans.append("YES")
    else:
        ans.append("NO")
for a in ans:
    print(a)
