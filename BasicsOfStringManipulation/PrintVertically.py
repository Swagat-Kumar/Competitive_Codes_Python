class Solution:
    def printVertically(self, s: str):
        ans = []
        words = s.split()
        lenn = 0
        for w in words:
            if len(w) > lenn:
                lenn = len(w)
        for i in range(lenn):
            temp = ''
            for w in words:
                if len(w) <= i:
                    temp += ' '
                else:
                    temp += w[i]
            temp = temp.rstrip()
            ans.append(temp)
        return ans
