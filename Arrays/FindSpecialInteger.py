class Solution:
    def findSpecialInteger(self, arr) -> int:
        n = len(arr)
        count = 0
        begin = arr[0]
        for a in arr:
            if a == begin:
                count += 1
            else:
                if count > 0.25*n:
                    return begin
                count = 1
                begin = a
        return begin
