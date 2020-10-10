class Solution:
    def toLowerCase(self, str: str) -> str:
        aux = ''
        for s in str:
            if ord(s) < 91 and ord(s) > 64:
                aux += chr(ord(s)+32)
            else:
                aux += s
        return aux
