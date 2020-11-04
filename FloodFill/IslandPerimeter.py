class Solution:
    def islandPerimeter(self, grid) -> int:
        def visit(x, y):
            if grid[x][y] == 1:
                return sideV(x-1, y)+sideV(x, y-1)+sideV(x+1, y)+sideV(x, y+1)
            else:
                return 0

        def sideV(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 1
            if grid[x][y] == 0:
                return 1
            return 0
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans += visit(r, c)
        return ans
