class Solution:
    def fib(self, N: int) -> int:
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        def fibb(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return fibb(n-1)+fibb(n-2)
        return fibb(N)
