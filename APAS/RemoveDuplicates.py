class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if i == 0:
                nums[k] = nums[i]
                k += 1
            elif nums[k-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
