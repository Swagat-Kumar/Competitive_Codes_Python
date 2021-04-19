class Solution:
    def findSubstring(self, s: str, words):
        ans = []
        if s == '' or len(words) == 0:
            return ans
        l = len(words[0])
        mapp = {}
        for w in words:
            if w in mapp:
                mapp[w] += 1
            else:
                mapp[w] = 1
        for i in range(len(s)-len(words)*l+1):
            copy = mapp.copy()
            for j in range(len(words)):
                sub = s[i+j*l:i+j*l+l]
                if sub in copy:
                    count = copy[sub]
                    if count == 1:
                        copy.pop(sub)
                    else:
                        copy[sub] = count-1
                    if not copy:
                        ans.append(i)
                        break
                else:
                    break
        return ans
