class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        aux = []
        for n in A:
            if n % 2 == 0:
                aux.append(n)
        for n in A:
            if n % 2 != 0:
                aux.append(n)
        return aux
