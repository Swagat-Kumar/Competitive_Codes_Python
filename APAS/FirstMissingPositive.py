class Solution:
    def firstMissingPositive(self, nums) -> int:
        for i in range(len(nums)):
            n = nums[i]
            while n-1 >= 0 and n-1 < len(nums) and nums[n-1] != n:
                nums[i] = nums[n-1]
                nums[n-1] = n
                n = nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
