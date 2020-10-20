class Solution:
    def maxDepth(self, s: str) -> int:
        lP = 0
        maxi = 0
        for c in s:
            if c == '(':
                lP += 1
                if lP > maxi:
                    maxi = lP
            elif c == ')':
                lP -= 1
        return maxi
