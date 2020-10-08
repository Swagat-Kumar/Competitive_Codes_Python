class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        iOne = 0
        iTwo = 0
        aux = [0]*(m+n)
        for i in range(m+n):
            if iOne >= m:
                aux[i] = nums2[iTwo]
                iTwo += 1
                continue
            elif iTwo >= n:
                aux[i] = nums1[iOne]
                iOne += 1
                continue
            if nums1[iOne] < nums2[iTwo]:
                aux[i] = nums1[iOne]
                iOne += 1
            else:
                aux[i] = nums2[iTwo]
                iTwo += 1
        for i in range(m+n):
            nums1[i] = aux[i]
