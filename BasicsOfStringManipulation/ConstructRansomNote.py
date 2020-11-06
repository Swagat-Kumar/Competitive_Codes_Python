class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lowers = [0]*26
        for l in magazine:
            lowers[ord(l)-97] += 1
        for r in ransomNote:
            if lowers[ord(r)-97] == 0:
                return False
            else:
                lowers[ord(r)-97] -= 1
        return True
