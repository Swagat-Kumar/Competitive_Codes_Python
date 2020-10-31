class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for a in arr:
            if a in freq:
                freq[a] += 1
                continue
            freq[a] = 1
        ans = -1
        for f in freq:
            if freq[f] == f:
                if f > ans:
                    ans = f
        return ans
