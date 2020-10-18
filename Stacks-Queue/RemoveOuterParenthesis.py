class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        lB = 0
        rB = 0
        aux = ''
        ans = ''
        for c in S:
            aux += c
            if c == '(':
                lB += 1
            else:
                rB += 1
            if lB == rB:
                ans += aux[1:len(aux)-1]
                aux = ''
        return ans
