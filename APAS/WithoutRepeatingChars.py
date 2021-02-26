s = input()
aux = [0]*128
ans = 0
j = 0
i = 0
for c in s:
    i = max(i, aux[ord(c)])
    ans = max(ans, j-i+1)
    aux[ord(c)] = j + 1
    j += 1
print(ans)
# st = input()
# aux = []
# maxLen = -1
# for c in st:
#     if c not in aux:
#         aux.append(c)
#         if len(aux) > maxLen:
#             maxLen = len(aux)
#     else:
#         aux = aux[len(aux)-aux[::-1].index(c):]
#         aux.append(c)
# if len(aux) > maxLen:
#     maxLen = len(aux)
# print(maxLen)
