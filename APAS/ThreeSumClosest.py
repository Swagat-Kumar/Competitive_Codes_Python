class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        closest = 10**9
        ans = -1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                aux = nums[i]+nums[j]+nums[k]
                if abs(aux-target) < closest:
                    closest = abs(aux-target)
                    ans = aux
                if aux <= target:
                    j += 1
                else:
                    k -= 1
        return ans
