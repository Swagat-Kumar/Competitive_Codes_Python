class Solution:
    def tribonacci(self, n: int) -> int:
        aux = [0]*(n+1)
        if n <= 1:
            return n
        aux[0] = 0
        aux[1] = 1
        aux[2] = 1
        for i in range(3, n+1):
            aux[i] = aux[i-1]+aux[i-2]+aux[i-3]
        return aux[n]
