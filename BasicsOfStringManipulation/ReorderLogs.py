class Solution:
    def reorderLogFiles(self, logs):
        listD = []
        listE = []
        for l in logs:
            ind = l.index(' ')
            if ord(l[ind+1]) >= 48 and ord(l[ind+1]) <= 57:
                listD.append(l)
            else:
                listE.append((l[ind+1:], l[:ind], l))
        listE.sort()
        aux = []
        for z in listE:
            aux.append(z[2])
        for c in listD:
            aux.append(c)
        return aux
