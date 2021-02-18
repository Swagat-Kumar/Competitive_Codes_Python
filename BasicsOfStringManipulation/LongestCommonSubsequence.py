class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        aux = [[0]*m for i in range(n)]

        def access(r, c):
            if r < 0 or c < 0:
                return 0
            else:
                return aux[r][c]
        maxLen = -1
        for r in range(len(aux)):
            for c in range(len(aux[r])):
                if text1[r] == text2[c]:
                    aux[r][c] = 1+access(r-1, c-1)
                else:
                    aux[r][c] = max(access(r, c-1), access(r-1, c))
                if aux[r][c] > maxLen:
                    maxLen = aux[r][c]
        return maxLen
