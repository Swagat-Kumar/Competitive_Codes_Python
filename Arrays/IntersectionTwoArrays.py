class Solution:
    def intersection(self, nums1, nums2):
        aux = []
        for n in nums1:
            if n in aux:
                continue
            aux.append(n)
        ans = []
        for n in aux:
            if n in nums2:
                ans.append(n)
        return ans
