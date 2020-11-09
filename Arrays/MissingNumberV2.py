class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        i = 0
        if nums[-1] != len(nums):
            return len(nums)
        while i < len(nums)+1:
            if nums[i] != i:
                return i
            i += 1
