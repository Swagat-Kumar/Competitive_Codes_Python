class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        cols = len(A[0])
        rows = len(A)
        listA = []
        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(A[r][c])
            listA.append(temp)
        return listA
