class Solution:
    def countBits(self, num: int):
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        def solve(num):
            if num <= 1:
                return num
            if num % 2 != 0:
                return 1+solve(num//2)
            else:
                return solve(num/2)
        solve = memoize(solve)
        aux = []
        for j in range(num+1):
            aux.append(solve(j))
        return aux
