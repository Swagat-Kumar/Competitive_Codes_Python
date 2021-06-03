class Solution:
    def search(self, nums, target: int) -> bool:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            print(mid, nums[mid])
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[low] and nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[mid] <= nums[high]:
                if target <= nums[high] and target > nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return False
