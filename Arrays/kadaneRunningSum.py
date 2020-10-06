class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = -2**31-1
        runningSum = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum > maxSum:
                maxSum = runningSum
            if runningSum < 0:
                runningSum = 0
        return maxSum
