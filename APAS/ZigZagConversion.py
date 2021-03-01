class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        aux = ['']*numRows
        i = 0
        down = True
        r = 0
        while i < len(s):
            if down:
                aux[r] += s[i]
                r += 1
                if r == numRows:
                    r = numRows-2
                    down = False
            else:
                aux[r] += s[i]
                r -= 1
                if r == -1:
                    r = 1
                    down = True
            i += 1
        ans = ''
        for a in aux:
            ans += a
        return ans
