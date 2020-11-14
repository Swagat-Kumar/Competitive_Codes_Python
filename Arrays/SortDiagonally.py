class Solution:
    def diagonalSort(self, mat):
        listA = []
        aux = []

        def visit(x, y):
            if x >= len(mat) or y >= len(mat[0]):
                return
            listA.append((x, y))
            aux.append(mat[x][y])
            visit(x+1, y+1)
        for c in range(len(mat[0])):
            visit(0, c)
            aux.sort()
            for k in range(len(aux)):
                mat[listA[k][0]][listA[k][1]] = aux[k]
            aux = []
            listA = []
        for r in range(1, len(mat)):
            visit(r, 0)
            aux.sort()
            for k in range(len(aux)):
                mat[listA[k][0]][listA[k][1]] = aux[k]
            aux = []
            listA = []
        return mat
