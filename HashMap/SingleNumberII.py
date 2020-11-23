class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for d in dic:
            if dic[d] != 3:
                return d
