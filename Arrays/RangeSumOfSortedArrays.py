class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        prefixSum = list(nums)
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1]+nums[i]
        possibleSums = list(prefixSum)
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                possibleSums.append(prefixSum[j]-prefixSum[i-1])
        possibleSums.sort()
        return sum(possibleSums[left-1:right]) % (10**9+7)
