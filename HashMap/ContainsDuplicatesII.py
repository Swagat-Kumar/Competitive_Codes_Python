class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
                continue
            if i-dic[nums[i]] <= k:
                return True
            else:
                dic[nums[i]] = i
        return False
