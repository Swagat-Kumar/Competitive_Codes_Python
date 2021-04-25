class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2**31-1
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return 2**31-1 if dividend == -2**31 else -dividend
        isNegative = (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0)
        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        temp = 0
        for i in range(31, -1, -1):
            if (temp+(divisor << i)) <= dividend:
                temp += divisor << i
                res |= 1 << i
        return -res if isNegative else res
