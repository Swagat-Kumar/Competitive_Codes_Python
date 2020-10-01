for t in range(1, 1001):
    n = t
    minn = n*100

    def recurr(curr=1, copy=0, step=0):
        global minn
        if curr > n:
            return
        if curr == n:
            if step < minn:
                minn = step
            return
        if copy > 0:
            recurr(curr+copy, copy, step+1)
        recurr(curr+curr, curr, step+2)
    recurr()
    print(t, " = ", minn)
