class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        def solve(num):
            if num == 0:
                return False
            if num == 1:
                return True
            if num % 4 == 0:
                return solve(num/4)
            else:
                return False
        return solve(num)
