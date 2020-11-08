class Solution:
    def checkIfExist(self, arr) -> bool:
        arr.sort()

        def binary(n):
            low = 0
            high = len(arr)-1
            while low <= high:
                mid = (low+high)//2
                if arr[mid] == n:
                    return True
                elif arr[mid] > n:
                    high = mid-1
                else:
                    low = mid+1
            return False
        for a in arr:
            if a == 0:
                count = 0
                for z in arr:
                    if z == 0:
                        count += 1
                        if count > 1:
                            break
                if count > 1:
                    return True
                continue
            if binary(a*2):
                return True
        return False
