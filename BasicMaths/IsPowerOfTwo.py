class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def solve(num):
            if num == 0:
                return False
            if num == 1:
                return True
            if num % 2 == 0:
                return solve(num/2)
            else:
                return False
        return solve(n)
