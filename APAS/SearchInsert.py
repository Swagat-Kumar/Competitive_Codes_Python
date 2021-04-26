class Solution:
    def searchInsert(self, nums, target: int) -> int:
        ans = 0
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        while nums[mid] < target:
            mid += 1
            if mid == len(nums):
                return mid
            if nums[mid] > target:
                return mid
        return mid
