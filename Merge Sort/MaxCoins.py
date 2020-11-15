class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort()
        i = 0
        ans = 0
        for j in range(len(piles)-2, -1, -2):
            if j < i:
                break
            ans += piles[j]
            i += 1
        return ans
