class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j] > 0:
                    break
                temp = nums[i]+nums[j]+nums[k]
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if temp > 0:
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return ans
