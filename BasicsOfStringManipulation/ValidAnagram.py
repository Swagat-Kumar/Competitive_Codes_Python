class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listA = [0]*26
        for c in s:
            listA[ord(c)-97] += 1
        for c in t:
            if listA[ord(c)-97] == 0:
                return False
            listA[ord(c)-97] -= 1
        for l in listA:
            if l != 0:
                return False
        return True
