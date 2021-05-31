class Solution:
    def climbStairs(self, n: int) -> int:
        aux = [0]*(n+1)
        aux[0] = 1
        for i in range(1, n+1):
            if i-2 >= 0:
                aux[i] += aux[i-2]
            aux[i] += aux[i-1]
        return aux[-1]
