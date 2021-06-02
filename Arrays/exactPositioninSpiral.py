n = int(input())
x = int(input())
level = 0
rang = (4*(n-2**level))
while x > rang and (n-2**level-1) > 0:
    level += 1
    rang += (4*(n-2*level-1))
print(level)
