class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = [[10**9]*(len(word2)+1) for i in range(len(word1)+1)]
        dp[0][0] = 0
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
        # if len(word1)==0:
        #     return len(word2)
        # if len(word2)==0:
        #     return len(word1)
        # if word1[0]==word2[0]:
        #     return self.minDistance(word1[1:],word2[1:])
        # else:
        #     return 1+min(self.minDistance(word1[1:],word2),self.minDistance(word1[1:],word2[1:]),self.minDistance(word1,word2[1:]))
