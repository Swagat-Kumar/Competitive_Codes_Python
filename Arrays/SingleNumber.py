class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        var = []
        for n in nums:
            if n not in dic:
                dic[n] = 1
                var.append(n)
            else:
                dic[n] += 1
        for v in var:
            if dic[v] == 1:
                return v
