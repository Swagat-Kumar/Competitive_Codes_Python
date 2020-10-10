class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)-1
        col = 0
        count = 0
        while grid[row][col] >= 0:
            col += 1
            if col >= len(grid[0]):
                return 0
        for c in range(col, len(grid[0])):
            r = row
            while grid[r][c] < 0:
                count += 1
                r -= 1
                if r < 0:
                    break
        return count
