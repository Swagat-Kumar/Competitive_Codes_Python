class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False
        start = 0
        while start < len(arr)-1:
            if arr[start] >= arr[start+1]:
                break
            start += 1
        if start == 0:
            return False
        end = len(arr)-1
        while end > -1:
            if arr[end] >= arr[end-1]:
                break
            end = end-1
        if end == len(arr)-1:
            return False
        return end == start
