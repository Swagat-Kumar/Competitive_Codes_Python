class Solution:
    def generateTheString(self, n: int) -> str:
        x = n
        if n % 2 == 0:
            x = n-1
        aux = 'x'*x+'y'*(n-x)
        return aux
