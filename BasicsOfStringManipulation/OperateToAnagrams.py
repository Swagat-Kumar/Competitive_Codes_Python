class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def returnCounts(st):
            listA = [0]*26
            for c in st:
                listA[ord(c)-97] += 1
            return listA
        listS = returnCounts(s)
        listT = returnCounts(t)
        ans = 0
        for i in range(26):
            if listT[i] > listS[i]:
                ans += listT[i]-listS[i]
        return ans
