class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        aux1 = []

        def returnAux(st):
            aux1 = []
            for c in st:
                if c == '#':
                    if len(aux1) > 0:
                        aux1.pop()
                else:
                    aux1.append(c)
            return ''.join(aux1)
        if returnAux(S) == returnAux(T):
            return True
        return False
