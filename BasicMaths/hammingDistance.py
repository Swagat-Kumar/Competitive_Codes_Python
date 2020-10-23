class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def hamm(a, b):
            if a == 0 and b == 0:
                return 0
            if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
                return hamm(a//2, b//2)
            else:
                return 1+hamm(a//2, b//2)
        return hamm(x, y)
