class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        points.sort()
        ans = 0
        for i in range(1, len(points)):
            if points[i][0]-points[i-1][0] > ans:
                ans = points[i][0]-points[i-1][0]
        return ans
