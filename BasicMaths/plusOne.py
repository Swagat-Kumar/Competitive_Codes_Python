class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for d in digits:
            n = n*10+d
        n += 1
        return list(str(n))
