def mHelper(pattern):
    helper = '|'
    for p in pattern:
        helper += p+'|'
    return helper


def manchar(text):
    backup = text
    text = mHelper(text)
    c = 0
    r = 0
    p = [0]*len(text)
    for i in range(1, len(text)-1):
        iMirror = 2*c-i
        if (r > i):
            p[i] = min(p[iMirror], r-i)
        try:
            while(text[i+p[i]+1] == text[i-p[i]-1]):
                p[i] += 1
        except:
            pass
        if i+p[i] > r:
            c = i
            r = i+p[i]
    maxLen = -1
    maxPos = -1

    for i in range(1, len(text)-1):
        if p[i] > maxLen:
            maxLen = p[i]
            maxPos = i
    start = (maxPos-maxLen)//2
    end = (maxPos+maxLen)//2
    return backup[start:end]


l = int(input())
s = manchar(input())
d = 0
while len(s) % 2 == 0 and s == s[::-1]:
    s = s[:len(s)//2]
    s = manchar(s)
    d += 1
print(d)
print(s)
