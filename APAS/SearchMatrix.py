class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        r = 0
        low = 0
        high = len(matrix)-1
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                r = mid
                break
            elif matrix[mid][-1] < target:
                low = mid+1
            else:
                high = mid-1
        low = 0
        high = len(matrix[0])-1
        while low <= high:
            mid = (low+high)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                high = mid-1
            else:
                low = mid+1
        return False
