class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low = 1
        high = x//2
        while low < high:
            mid = (high-low+1)//2+low
            t = x//mid
            if t == mid:
                return mid
            elif mid > t:
                high = mid-1
            else:
                low = mid
        return high
