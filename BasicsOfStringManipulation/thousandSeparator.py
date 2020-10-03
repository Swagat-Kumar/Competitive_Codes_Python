class Solution:
    def thousandSeparator(self, n: int) -> str:
        x = 3
        aux = list(str(n))
        ans = ''
        while len(aux) != 0:
            i = 0
            temp = ''
            while i < 3 and len(aux) != 0:
                temp = aux.pop()+temp
                i += 1
            if n > 10**x:
                ans = '.'+temp+ans
                x += 3
            else:
                ans = temp+ans
        return ans
