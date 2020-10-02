class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        marked = [[False]*len(grid[0]) for i in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    marked[r][c] = True

        def visit(r, c, markL):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            if markL[r][c]:
                return 0
            copy = list(map(list, markL))
            copy[r][c] = True
            return grid[r][c]+max(visit(r+1, c, copy), visit(r-1, c, copy), visit(r, c-1, copy), visit(r, c+1, copy))
        maximum = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not marked[r][c]:
                    maximum = max(maximum, visit(r, c, marked))
        print(marked)
        return maximum
