class Solution:
    def hammingWeight(self, n: int) -> int:
        def count(num):
            if num <= 1:
                return num
            if num % 2 == 0:
                return count(num//2)
            else:
                return 1+count(num//2)
        return count(n)
