class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nWays = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    nWays[r][c] = 1
                    continue
                if r == 0:
                    nWays[r][c] += nWays[r][c-1]
                    continue
                if c == 0:
                    nWays[r][c] += nWays[r-1][c]
                    continue
                nWays[r][c] = nWays[r-1][c]+nWays[r][c-1]
        return nWays[-1][-1]
