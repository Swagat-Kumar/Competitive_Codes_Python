class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        rows = [0]*len(grid)
        cols = [0]*len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows[r] += 1
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    cols[c] += 1
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if rows[r] > 1 or cols[c] > 1:
                        count += 1
        return count
