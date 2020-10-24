class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            maxinRow = -1
            for c in range(len(grid)):
                if grid[r][c] != 0:
                    ans += 1
                if grid[r][c] > maxinRow:
                    maxinRow = grid[r][c]
            ans += maxinRow
        for c in range(len(grid)):
            maxinCol = -1
            for r in range(len(grid)):
                if grid[r][c] > maxinCol:
                    maxinCol = grid[r][c]
            ans += maxinCol
        return ans
