class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isCal = False
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                isCal = True
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if isCal:
            for r in range(len(matrix)):
                matrix[r][0] = 0


# Myway
# class Solution:
#     def setZeroes(self, matrix) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         zeroRows = [False]*len(matrix)
#         zeroColoumns = [False]*len(matrix[0])
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c] == 0:
#                     zeroRows[r] = True
#                     zeroColoumns[c] = True
#         for r in range(len(matrix)):
#             if zeroRows[r]:
#                 for c in range(len(matrix[0])):
#                     matrix[r][c] = 0
#         for c in range(len(matrix[0])):
#             if zeroColoumns[c]:
#                 for r in range(len(matrix)):
#                     matrix[r][c] = 0
