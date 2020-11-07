import bisect


class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(s):
            listA = [0]*26
            for c in s:
                listA[ord(c)-97] += 1
            for l in listA:
                if l != 0:
                    return l
        wordS = []
        for w in words:
            wordS.append(f(w))
        wordS.sort()
        ans = []
        for q in queries:
            ans.append(len(wordS)-bisect.bisect_right(wordS, f(q)))
        return ans
