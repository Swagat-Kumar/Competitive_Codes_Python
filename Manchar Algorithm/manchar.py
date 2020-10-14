def mHelper(pattern):
    help = '|'
    for p in pattern:
        help += p+'|'
    return help


def manchar(text):
    text = mHelper(text)
    c = 0
    r = 0
    p = [0]*len(text)
    maxPos = -1
    maxLen = -1
    for i in range(1, len(text)-1):
        iMirror = 2*c-i
        if r > i:
            p[i] = min(p[iMirror], r-i)
        try:
            while text[i+p[i]+1] == text[i-p[i]-1]:
                p[i] += 1
        except:
            pass
        if i+p[i] > r:
            c = i
            r = i+p[i]
    print(p)
    for i in range(1, len(text)-1):
        if p[i] > maxLen:
            maxLen = p[i]
            maxPos = i
    return ((maxPos-maxLen)//2, (maxPos+maxLen)//2)


print(manchar('aabbaa'))
