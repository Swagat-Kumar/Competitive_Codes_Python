class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def check(st, x, i):
            if x <= 0:
                return False
            return st[x-1] == s3[i-1]

        def memoize(f):
            memo = {}

            def helper(x, y, z):
                if (x, y, z) not in memo:
                    memo[(x, y, z)] = f(x, y, z)
                return memo[(x, y, z)]
            return helper

        def solve(n, m, i):
            if i == 0:
                if n == 0 and m == 0:
                    return True
                else:
                    return False
            if check(s1, n, i) and check(s2, m, i):
                return solve(n-1, m, i-1) or solve(n, m-1, i-1)
            elif check(s1, n, i):
                return solve(n-1, m, i-1)
            elif check(s2, m, i):
                return solve(n, m-1, i-1)
            else:
                return False
        return solve(len(s1), len(s2), len(s3))
