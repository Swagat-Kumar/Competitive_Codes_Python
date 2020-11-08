class NumArray:

    def __init__(self, nums):
        self.prefixSum = [0]*len(nums)
        if len(nums) == 0:
            return
        self.prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefixSum[i] = self.prefixSum[i-1]+nums[i]
        print(self.prefixSum)

    def sumRange(self, i: int, j: int) -> int:
        if i-1 < 0:
            return self.prefixSum[j]
        return self.prefixSum[j]-self.prefixSum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
