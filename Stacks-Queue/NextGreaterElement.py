class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            if len(stack) != 0:
                while len(stack) != 0 and stack[-1] < nums2[i]:
                    stack.pop()
                    if len(stack) == 0:
                        break
            if len(stack) == 0:
                dic[nums2[i]] = -1
            else:
                dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        ans = []
        for n in nums1:
            ans.append(dic[n])
        return ans
