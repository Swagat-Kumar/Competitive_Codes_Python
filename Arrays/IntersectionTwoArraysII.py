class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        k = 0
        aux = []
        while i < len(nums1) and k < len(nums2):
            if nums1[i] > nums2[k]:
                k += 1
            elif nums1[i] < nums2[k]:
                i += 1
            else:
                aux.append(nums1[i])
                i += 1
                k += 1
        return aux
