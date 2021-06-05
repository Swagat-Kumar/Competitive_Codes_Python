class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ans = max(ans, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            ans = max(ans, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return ans
