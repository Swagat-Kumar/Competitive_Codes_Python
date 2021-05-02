class Solution:
    def jump(self, nums) -> int:
        jump = [9999]*len(nums)
        jump[0] = 0
        for i in range(len(nums)):
            for k in range(i+1, i+nums[i]+1):
                if k >= len(nums):
                    break
                jump[k] = min(jump[i]+1, jump[k])
        return jump[-1]
