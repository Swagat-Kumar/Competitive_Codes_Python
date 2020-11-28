class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        rowsky = []
        colsky = []
        for r in range(len(grid)):
            maxx = -1
            for c in range(len(grid[0])):
                if grid[r][c] > maxx:
                    maxx = grid[r][c]
            rowsky.append(maxx)
        for c in range(len(grid[0])):
            maxx = -1
            for r in range(len(grid)):
                if grid[r][c] > maxx:
                    maxx = grid[r][c]
            colsky.append(maxx)
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == colsky[c] or grid[r][c] == rowsky[r]:
                    continue
                ans += min(colsky[c], rowsky[r])-grid[r][c]
        return ans
