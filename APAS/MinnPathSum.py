class Solution:
    def minPathSum(self, grid) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    continue
                sett = []
                if r-1 >= 0:
                    sett.append(grid[r-1][c])
                if c-1 >= 0:
                    sett.append(grid[r][c-1])
                grid[r][c] = grid[r][c]+min(sett)
        return grid[-1][-1]
