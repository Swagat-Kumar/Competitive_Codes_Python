class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        ans = 0
        aux = 1
        for c in s:
            ans += (ord(c)-64)*aux
            aux *= 26
        return ans
