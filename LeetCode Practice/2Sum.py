import bisect


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        aux = list(nums)
        aux.sort()
        left = 0
        right = len(aux)-1
        while left != right:
            if(aux[left]+aux[right] > target):
                right -= 1
                continue
            if(aux[left]+aux[right] < target):
                left += 1
                continue
            if(aux[left]+aux[right] == target):
                break
        if(aux[left]+aux[right] == target and left != right):
            print(aux[left], aux[right])
            ans.append(nums.index(aux[left]))
            ans.append(len(nums)-1-nums[::-1].index(aux[right]))
            ans.sort()
        return ans
