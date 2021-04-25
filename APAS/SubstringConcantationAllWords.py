class Solution:
    def findSubstring(self, s: str, words):
        dic = {}
        for w in words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        l = len(words[0])
        ans = []
        for i in range(len(s)-len(words)*len(words[0])+1):
            copy = dic.copy()
            for j in range(len(words)):
                extract = s[i+j*l:i+j*l+l]
                if extract in copy:
                    if copy[extract] == 1:
                        del copy[extract]
                    else:
                        copy[extract] -= 1
                    if not copy:
                        ans.append(i)
                else:
                    break
        return ans
