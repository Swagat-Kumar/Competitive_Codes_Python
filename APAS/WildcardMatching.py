class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0] = True
        for c in range(1, len(dp[0])):
            if p[c-1] == '*':
                dp[0][c] = True
            else:
                break
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r == 0 or c == 0:
                    continue
                if p[c-1] != '*':
                    dp[r][c] = dp[r-1][c -
                                       1] and (s[r-1] == p[c-1] or p[c-1] == '?')
                else:
                    dp[r][c] = dp[r-1][c] or dp[r][c-1]
        return dp[-1][-1]
