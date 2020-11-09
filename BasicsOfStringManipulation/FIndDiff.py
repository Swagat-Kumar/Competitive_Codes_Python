class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        listS = [0]*26
        listT = [0]*26
        for c in s:
            listS[ord(c)-97] += 1
        for c in t:
            listT[ord(c)-97] += 1
        for i in range(26):
            if listT[i] != listS[i]:
                return chr(97+i)
