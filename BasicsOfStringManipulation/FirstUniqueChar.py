class Solution:
    def firstUniqChar(self, s: str) -> int:
        lowers = [0]*26
        for c in s:
            lowers[ord(c)-97] += 1
        for i in range(len(s)):
            if lowers[ord(s[i])-97] == 1:
                return i
        return -1
