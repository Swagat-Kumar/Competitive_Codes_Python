class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
