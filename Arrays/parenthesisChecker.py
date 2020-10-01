# code
lt = ['{', '[', '(']
rt = ['}', ']', ')']
t = int(input())
for tt in range(t):
    line = input()
    q = []
    ans = True
    for l in line:
        if l in lt:
            q.append(l)
        else:
            if len(q) == 0:
                ans = False
                break
            temp = q.pop()
            if lt.index(temp) != rt.index(l):
                ans = False
                break
    if ans and len(q) == 0:
        print('balanced')
    else:
        print('not balanced')
