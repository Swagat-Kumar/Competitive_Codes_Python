class Solution:
    def minFallingPathSum(self, A) -> int:
        self.minn = 10**7

        def helper(r, c):
            if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]):
                return 10**7
            else:
                return A[r][c]
        for r in range(1, len(A)):
            for c in range(len(A[0])):
                A[r][c] = min(helper(r-1, c), helper(r-1, c+1),
                              helper(r-1, c-1))+A[r][c]
        return min(A[-1])
