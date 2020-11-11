class Solution:
    def findErrorNums(self, nums):
        listA = [0]*(len(nums)+1)
        for n in nums:
            listA[n] += 1
        first = 0
        second = 0
        for i in range(1, len(nums)+1):
            if listA[i] == 0:
                first = i
            elif listA[i] == 2:
                second = i
        return [second, first]
