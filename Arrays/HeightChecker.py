class Solution:
    def heightChecker(self, heights) -> int:
        copy = list(heights)
        heights.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != copy[i]:
                count += 1
        return count
