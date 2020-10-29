class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        def power(n):
            if n <= 1:
                return 0
            if n % 2 == 0:
                return 1+power(n/2)
            else:
                return 1+power(3*n+1)
        power = memoize(power)
        aux = []
        for i in range(lo, hi+1):
            aux.append((power(i), i))
        aux.sort()
        return aux[k-1][1]
