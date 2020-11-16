class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        visitx = [[False]*len(grid[0]) for i in range(len(grid))]

        def visit(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            if visitx[r][c]:
                return 0
            if grid[r][c] == 1:
                visitx[r][c] = True
                return 1+visit(r-1, c)+visit(r+1, c)+visit(r, c-1)+visit(r, c+1)
            else:
                return 0
        maxx = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visitx[r][c]:
                    val = visit(r, c)
                    if val > maxx:
                        maxx = val
        return maxx
