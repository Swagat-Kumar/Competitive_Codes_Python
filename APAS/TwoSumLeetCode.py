class Solution:
    def twoSum(self, nums, target: int):
        aux = {}
        i = 0
        for n in nums:
            compliment = target-n
            if compliment in aux:
                return [aux[compliment], i]
            aux[n] = i
            i += 1
