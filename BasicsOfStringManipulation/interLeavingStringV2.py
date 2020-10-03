class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False

        def memoize(f):
            memo = {}

            def helper(x, y):
                if (x, y) not in memo:
                    memo[(x, y)] = f(x, y)
                return memo[(x, y)]
            return helper

        def recurr(n, m):
            if n == 0 and m == 0:
                return True
            if n == 0:
                if s2[m-1] == s3[m-1]:
                    return recurr(n, m-1)
                else:
                    return False
            if m == 0:
                if s1[n-1] == s3[n-1]:
                    return recurr(n-1, m)
                else:
                    return False
            if s1[n-1] == s2[m-1] == s3[n+m-1]:
                return recurr(n-1, m) or recurr(n, m-1)
            elif s1[n-1] == s3[n+m-1]:
                return recurr(n-1, m)
            elif s2[m-1] == s3[n+m-1]:
                return recurr(n, m-1)
            return False
        recurr = memoize(recurr)
        return recurr(len(s1), len(s2))
