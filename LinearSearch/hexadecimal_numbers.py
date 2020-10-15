import math
t = int(input())
ans = []


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def hexFunction(j):

    value = 0
    hexString = hex(j).lstrip("0x").rstrip("L")
    for k in hexString:
        m = ord(k)
        if(m > 96):
            value += 10+m-97
        else:
            value += int(k)

    return value


hexFunc = memoize(hexFunction)

for i in range(t):
    line = list(map(int, input().split(" ")))
    l = line[0]
    r = line[1]
    testAnswer = 0
    for j in range(l, r+1):
        if(math.gcd(j, hexFunc(j)) > 1):
            testAnswer += 1
    ans.append(testAnswer)
for a in ans:
    print(a)
