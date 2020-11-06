class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def solve(num):
            if num == 0:
                return False
            if num == 1:
                return True
            if num % 3 == 0:
                return solve(num/3)
            else:
                return False
        return solve(n)
