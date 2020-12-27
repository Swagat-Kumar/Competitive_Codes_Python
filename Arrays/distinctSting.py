t = int(input())
for tt in range(t):
    st = input()
    di = []
    ma = -1
    for s in st:
        if s not in di:
            di.append(s)
        else:
            if len(di) > ma:
                ma = len(di)
            di = di[di.index(s):]
    print(ma)
