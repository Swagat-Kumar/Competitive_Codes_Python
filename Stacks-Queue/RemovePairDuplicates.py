class Solution:
    def removeDuplicates(self, S: str) -> str:
        def removeStep(st):
            aux = []
            for s in st:
                if len(aux) == 0:
                    aux.append(s)
                    continue
                if s == aux[-1]:
                    aux.pop()
                    continue
                else:
                    aux.append(s)
            return ''.join(aux)
        aux = removeStep(S)
        while aux != S:
            S = aux
            aux = removeStep(S)
        return S
