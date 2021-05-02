class Solution:
    def trap(self, height) -> int:
        leftMax = 0
        rightMax = 0
        lo = 0
        hi = len(height)-1
        ans = 0
        while lo < hi:
            if height[lo] < height[hi]:
                if height[lo] >= leftMax:
                    leftMax = height[lo]
                else:
                    ans += (leftMax-height[lo])
                lo += 1
            else:
                if height[hi] >= rightMax:
                    rightMax = height[hi]
                else:
                    ans += (rightMax-height[hi])
                hi -= 1
        return ans
