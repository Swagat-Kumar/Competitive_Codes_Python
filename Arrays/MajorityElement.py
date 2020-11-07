class Solution:
    def majorityElement(self, nums) -> int:
        length = len(nums)//2
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
                if dic[n] > length:
                    return n
        for d in dic:
            if dic[d] > length:
                return d
