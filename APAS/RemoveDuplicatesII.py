class Solution:
    def removeDuplicates(self, nums) -> int:
        dn = {}
        k = 0
        for n in nums:
            if n not in dn:
                dn[n] = 1
            else:
                dn[n] += 1
            if dn[n] > 2:
                continue
            nums[k] = n
            k += 1
        return k
