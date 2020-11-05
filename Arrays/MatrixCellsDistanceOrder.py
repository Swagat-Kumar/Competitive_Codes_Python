class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        aux = []
        for r in range(R):
            for c in range(C):
                aux.append((abs(r-r0)+abs(c-c0), r, c))
        aux.sort()
        ans = []
        while len(aux) != 0:
            popped = aux.pop(0)
            ans.append([popped[1], popped[2]])
        return ans
