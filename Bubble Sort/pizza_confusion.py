n = int(input())
ansPoint = -1
ans = ""
for i in range(n):
    name, point = input().split()
    point = int(point)
    if(point > ansPoint):
        ans = name
        ansPoint = point
    elif (point == ansPoint):
        if(name < ans):
            ans = name
            ansPoint = point
print(ans)
