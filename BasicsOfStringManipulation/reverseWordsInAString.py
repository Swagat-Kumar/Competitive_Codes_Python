class Solution:
    def reverseWords(self, s: str) -> str:
        aux = ''
        for t in list(s.split()):
            aux += t[::-1]+' '
        return aux[:len(aux)-1]
