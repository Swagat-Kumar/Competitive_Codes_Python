class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        matrix = [[0]*len(grid[0])for i in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    matrix[r][c] = grid[r][c]
                    continue
                if r == 0:
                    matrix[r][c] = grid[r][c]+matrix[r][c-1]
                    continue
                if c == 0:
                    matrix[r][c] = grid[r][c]+matrix[r-1][c]
                    continue
                matrix[r][c] = grid[r][c]+min(matrix[r-1][c], matrix[r][c-1])
        return matrix[-1][-1]
