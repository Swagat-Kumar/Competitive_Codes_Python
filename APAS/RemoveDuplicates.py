class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        i = 1
        k = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
