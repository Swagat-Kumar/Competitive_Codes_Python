from math import floor


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        self.ones = 0
        self.n = 0

        def visit(r, c):
            if r < 0 or c < 0 or r >= len(M) or c >= len(M[0]):
                return
            self.ones += M[r][c]
            self.n += 1
        listA = [[0]*len(M[0]) for i in range(len(M))]
        for r in range(len(M)):
            for c in range(len(M[0])):
                for rr in range(-1, 2):
                    for cc in range(-1, 2):
                        visit(rr+r, cc+c)
                listA[r][c] = floor(self.ones/self.n)
                self.ones = 0
                self.n = 0
        return listA
