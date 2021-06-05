class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [0]*n
        right = [n]*n
        height = [0]*n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            leftB = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], leftB)
                else:
                    left[j] = 0
                    leftB = j+1
            rightB = n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], rightB)
                else:
                    right[j] = n
                    rightB = j
            for j in range(n):
                ans = max(ans, (right[j]-left[j])*height[j])
        return ans
