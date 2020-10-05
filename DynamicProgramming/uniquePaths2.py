class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0
        nWays = [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if r == 0 and c == 0:
                    nWays[r][c] = 1
                    continue
                if r == 0:
                    if obstacleGrid[r][c-1] == 0:
                        nWays[r][c] += nWays[r][c-1]
                    continue
                if c == 0:
                    if obstacleGrid[r-1][c] == 0:
                        nWays[r][c] += nWays[r-1][c]
                    continue
                if obstacleGrid[r][c-1] == 0:
                    nWays[r][c] += nWays[r][c-1]
                if obstacleGrid[r-1][c] == 0:
                    nWays[r][c] += nWays[r-1][c]
        return nWays[-1][-1]
