class Solution:
    def findDuplicates(self, nums):
        listA = [0]*(len(nums)+1)
        for n in nums:
            listA[n] += 1
        aux = []
        for i in range(1, len(nums)+1):
            if listA[i] == 2:
                aux.append(i)
        return aux
