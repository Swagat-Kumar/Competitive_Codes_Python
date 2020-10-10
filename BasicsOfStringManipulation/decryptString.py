class Solution:
    def freqAlphabets(self, s: str) -> str:
        print(ord('a'))
        end = len(s)-1
        aux = ''
        while end > -1:
            x = s[end]
            if x == '#':
                x = s[end-2:end]
                end -= 2
            x = int(x)
            aux = chr(96+x)+aux
            end -= 1
        return aux
