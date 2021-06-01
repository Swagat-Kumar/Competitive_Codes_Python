class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        whiteEnd = 0
        redEnd = 0
        for i in range(len(nums)):
            save = nums[i]
            nums[i] = 2
            if save == 0:
                nums[whiteEnd] = 1
                whiteEnd += 1
                nums[redEnd] = 0
                redEnd += 1
            elif save == 1:
                nums[whiteEnd] = 1
                whiteEnd += 1
