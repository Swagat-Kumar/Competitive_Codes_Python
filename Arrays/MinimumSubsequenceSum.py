class Solution:
    def minSubsequence(self, nums):
        nums.sort()
        sumA = sum(nums)
        currentSum = 0
        listA = []
        for i in range(len(nums)):
            currentSum += nums[len(nums)-1-i]
            listA.append(nums[len(nums)-1-i])
            if currentSum > sumA-currentSum:
                break
        return listA
