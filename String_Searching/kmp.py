def computeLPS(pattern):
    m = len(pattern)
    le = 0
    lps = [0]*m
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[le]:
            le += 1
            lps[i] = le
            i += 1
        elif le != 0:
            le = lps[le-1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmpSearch(pattern, txt):
    m = len(pattern)
    n = len(txt)
    i = 0
    j = 0
    count = 0
    lps = computeLPS(pattern)
    while i < n:
        if pattern[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j-1]
        elif i < n and pattern[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return count


print(kmpSearch('abc', 'abcabc'))
print(str(int('000126')))
