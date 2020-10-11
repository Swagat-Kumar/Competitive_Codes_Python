class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        aux = list(A)
        for i in range(len(aux)):
            if aux[i] < 0:
                aux[i] = -aux[i]
        aux.sort()
        for i in range(len(aux)):
            aux[i] = aux[i]**2
        return aux
