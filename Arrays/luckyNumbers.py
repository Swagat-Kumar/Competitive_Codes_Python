class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minr = [0]*len(matrix)
        maxc = [0]*len(matrix[0])
        for i in range(len(matrix)):
            minR = 10**7
            for j in range(len(matrix[0])):
                if minR > matrix[i][j]:
                    minR = matrix[i][j]
            minr[i] = minR
        print(minr)
        for i in range(len(matrix[0])):
            minR = -10
            for j in range(len(matrix)):
                if minR < matrix[j][i]:
                    minR = matrix[j][i]
            maxc[i] = minR
        print(maxc)
        listA = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == minr[r] and matrix[r][c] == maxc[c]:
                    listA.append(matrix[r][c])
        return listA
