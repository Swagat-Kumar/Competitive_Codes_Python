class Solution:
    def findWords(self, words):
        listA = []
        aux = {0: 'QWERTYUIOP', 1: 'ASDFGHJKL', 2: 'ZXCVBNM'}

        def contains(c, i):
            return c in aux[i] or chr(ord(c)-32) in aux[i]
        for w in words:
            z = 0
            add = True
            i = 0
            for i in range(3):
                if contains(w[0], i):
                    break
            for j in w:
                if not contains(j, i):
                    add = False
                    break
            if add:
                listA.append(w)
        return listA
