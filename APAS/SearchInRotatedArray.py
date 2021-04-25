class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid-1
                else:
                    lo = mid+1
            if nums[mid] <= nums[hi]:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1
