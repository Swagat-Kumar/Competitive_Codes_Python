class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        listZ = [0]*len(s)
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            listZ[i] = zeros
        ones = 0
        listO = [0]*len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                ones += 1
            listO[i] = ones
        maxx = 0
        for i in range(len(s)-1):
            if listZ[i]+listO[i+1] > maxx:
                maxx = listZ[i]+listO[i+1]
        return maxx
