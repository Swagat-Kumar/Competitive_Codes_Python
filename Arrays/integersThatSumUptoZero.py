class Solution:
    def sumZero(self, n: int) -> List[int]:
        start = 1
        if n % 2 == 0:
            aux = []
        else:
            aux = [0]
        while len(aux) != n:
            aux.append(start)
            aux.append(-start)
            start += 1
        return aux
