class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(text):
            aux = '|'
            for t in text:
                aux += t+'|'
            return aux

        def manchar(text):
            originalText = text
            text = helper(text)
            c = 0
            r = 0
            p = [0]*len(text)
            for i in range(1, len(text)-1):
                iMirror = 2*c-i
                if r > i:
                    p[i] = min(p[iMirror], r-i)
                try:
                    while(text[i+p[i]+1] == text[i-p[i]-1]):
                        p[i] += 1
                except:
                    pass
                if i+p[i] > r:
                    c = i
                    r = i+p[i]
            maxLen = -1
            maxPos = -1
            for i in range(1, len(text)-1):
                if p[i] > maxLen:
                    maxLen = p[i]
                    maxPos = i
            return originalText[(maxPos-maxLen)//2:(maxPos+maxLen)//2]

        return manchar(s)
