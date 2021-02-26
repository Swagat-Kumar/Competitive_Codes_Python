class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aux = [0]*128
        i = 0
        j = 0
        ans = 0
        for c in s:
            i = max(i, aux[ord(c)])
            ans = max(ans, j-i+1)
            aux[ord(c)] = j+1
            j += 1
        return ans
