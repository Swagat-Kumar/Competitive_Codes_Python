# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# just to avoid error make infinite loop


def guess(n):
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (start+end)//2
            if guess(mid) == 0:
                return mid
            if guess(mid) < 0:
                end = mid-1
            else:
                start = mid+1
