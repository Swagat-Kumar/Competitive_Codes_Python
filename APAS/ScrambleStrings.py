class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def scramble(s1, s2):
            if len(s1) != len(s2):
                return False
            n = len(s1)
            if n == 0:
                return True
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1, n):
                if scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:]):
                    return True
                if scramble(s1[:i], s2[-i:]) and scramble(s1[i:], s2[:-i]):
                    return True
            return False

        def memoize(f):
            memo = {}

            def helper(x, y):
                if x+'|'+y not in memo:
                    memo[x+'|'+y] = f(x, y)
                return memo[x+'|'+y]
            return helper
        scramble = memoize(scramble)
        return scramble(s1, s2)
