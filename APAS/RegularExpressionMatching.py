class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dynamicMatch = [[False]*(len(p)+1) for i in range(len(s)+1)]
        dynamicMatch[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                firstMatch = False
                if i < len(s):
                    firstMatch = s[i] == p[j] or p[j] == '.'
                if j+1 < len(p):
                    if p[j+1] == '*':
                        dynamicMatch[i][j] = (
                            firstMatch and dynamicMatch[i+1][j]) or dynamicMatch[i][j+2]
                        continue
                dynamicMatch[i][j] = firstMatch and dynamicMatch[i+1][j+1]
        return dynamicMatch[0][0]


# for i in range(5):
#     s = input()
#     p = input()
#     print(isMatch(s, p))
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if len(p) == 0:
#             return len(s) == 0
#         firstMatch = False
#         if len(s) != 0:
#             firstMatch = s[0] == p[0] or p[0] == '.'
#         if len(p) >= 2:
#             if p[1] == '*':
#                 return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
#         return firstMatch and self.isMatch(s[1:], p[1:])
