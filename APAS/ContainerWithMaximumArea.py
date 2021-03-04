class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height)-1
        maxArea = -1
        while i < j:
            area = min(height[i], height[j])*(j-i)
            if area > maxArea:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return maxArea
