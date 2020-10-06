class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        matrix = list(nums)
        for i in range(1, len(nums)):
            matrix[i] = matrix[i-1]+nums[i]
        return matrix
