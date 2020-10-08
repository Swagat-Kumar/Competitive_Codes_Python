class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        iO = m
        iT = n
        for i in range(m+n-1, -1, -1):
            if iO == 0:
                nums1[i] = nums2[iT-1]
                iT -= 1
                continue
            elif iT == 0:
                nums1[i] = nums1[iO-1]
                iO -= 1
            if nums1[iO-1] > nums2[iT-1]:
                nums1[i] = nums1[iO-1]
                iO -= 1
            else:
                nums1[i] = nums2[iT-1]
                iT -= 1
