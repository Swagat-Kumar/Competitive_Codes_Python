class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 2:
            return []
        if nums[len(nums)-1] < 0:
            return []
        ans = []
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            if nums[i] > 0:
                break
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            while start < end:
                if end < len(nums)-1 and end > i+1 and nums[end] == nums[end+1]:
                    end -= 1
                    continue
                if nums[start]+nums[end]+nums[i] == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    continue
                if nums[start]+nums[end]+nums[i] > 0:
                    end -= 1
                else:
                    start += 1
        return ans
