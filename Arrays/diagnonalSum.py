class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumA = 0
        x = 0
        y = 0
        while x < len(mat):
            sumA += mat[x][y]
            x += 1
            y += 1
        x = 0
        y = len(mat)-1
        while x < len(mat):
            if x != y:
                sumA += mat[x][y]
            x += 1
            y -= 1
        return sumA
