class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0]*n
        col = [0]*m
        for index in indices:
            row[index[0]] += 1
            col[index[1]] += 1
        count = 0
        for r in range(n):
            for c in range(m):
                if (row[r]+col[c]) % 2 != 0:
                    count += 1
        return count
