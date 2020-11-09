class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        listA = [False]*(n+1)
        for z in nums:
            listA[z] = True
        for i in range(n+1):
            if not listA[i]:
                return i
