class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s)+1):
            oneD = int(s[i-1:i])
            twoD = int(s[i-2:i])
            dp[i] = (0 if oneD == 0 else dp[i-1]) + \
                (dp[i-2] if (twoD > 9 and twoD < 27) else 0)
        return dp[-1]
