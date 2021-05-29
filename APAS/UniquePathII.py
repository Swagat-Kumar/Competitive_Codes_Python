class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*(m+1) for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if obstacleGrid[i-1][j-1]:
                    dp[i][j] = 0
                    continue
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
