class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sumA = 0
        for i in range(0, len(nums), 2):
            sumA += nums[i]
        return sumA
