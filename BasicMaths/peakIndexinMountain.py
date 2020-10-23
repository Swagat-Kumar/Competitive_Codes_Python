class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            if arr[i+1] > arr[i]:
                i += 1
            else:
                break
        return i
