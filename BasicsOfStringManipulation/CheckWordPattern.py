class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        listA = []
        for w in words:
            dic = {}
            add = True
            listC = []
            for i in range(len(w)):
                if w[i] not in dic:
                    if pattern[i] not in listC:
                        dic[w[i]] = pattern[i]
                        listC.append(pattern[i])
                    else:
                        add = False
                        break
                else:
                    if dic[w[i]] != pattern[i]:
                        add = False
                        break
            if add:
                listA.append(w)
        return listA
