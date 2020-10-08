class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for l in S:
            if l in J:
                count += 1
        return count
