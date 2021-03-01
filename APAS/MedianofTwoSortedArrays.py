class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        small = nums1 if len(nums1) <= len(nums2) else nums2
        large = nums2 if len(nums2) >= len(nums1) else nums1
        half = (len(small)+len(large)+1)//2
        iMax = len(small)
        iMin = 0
        while iMin <= iMax:
            i = (iMin+iMax)//2
            j = half-i
            leftMaxSmall = -10**8 if i == 0 else small[i-1]
            rightMinSmall = 10**8 if i == len(small) else small[i]
            leftMaxLarge = -10**8 if j == 0 else large[j-1]
            rightMinLarge = 10**8 if j == len(large) else large[j]
            if leftMaxSmall <= rightMinLarge and leftMaxLarge <= rightMinSmall:
                if (len(small)+len(large)) % 2 == 0:
                    return (max(leftMaxSmall, leftMaxLarge)+min(rightMinSmall, rightMinLarge))/2.0
                else:
                    return max(leftMaxSmall, leftMaxLarge)/1.0
            elif leftMaxSmall > rightMinLarge:
                iMax = i-1
            else:
                iMin = i+1
        return 0.0


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         k=0
#         i=0
#         j=0
#         merge=[]
#         while k<len(nums1)+len(nums2):
#             if i>=len(nums1):
#                 merge.append(nums2[j])
#                 j+=1
#             elif j>=len(nums2):
#                 merge.append(nums1[i])
#                 i+=1
#             elif nums1[i]<nums2[j]:
#                 merge.append(nums1[i])
#                 i+=1
#             else:
#                 merge.append(nums2[j])
#                 j+=1
#             k+=1
#         n=len(merge)
#         if n%2==0:
#             return (merge[len(merge)//2]+merge[len(merge)//2-1])/2
#         else:
#             return merge[len(merge)//2]
