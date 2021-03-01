class Solution:
    def reverse(self, x: int) -> int:
        n = x
        sign = -1 if n < 0 else 1
        x = 0
        n = abs(n)
        while n != 0:
            x = x*10+n % 10
            n = n//10
        ans = x*sign
        if ans < -2**31 or ans > 2**31-1:
            return 0
        else:
            return ans
