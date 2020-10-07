class Solution:
    def defangIPaddr(self, address: str) -> str:
        aux = ""
        for s in address:
            if s == '.':
                aux += '[.]'
            else:
                aux += s
        return aux
