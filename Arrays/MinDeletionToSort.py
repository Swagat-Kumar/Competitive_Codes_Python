class Solution:
    def minDeletionSize(self, A) -> int:
        count = 0
        for i in range(len(A[0])):
            canAdd = False
            for j in range(len(A)-1):
                if A[j+1][i] < A[j][i]:
                    canAdd = True
                    break
            if canAdd:
                count += 1
        return count
