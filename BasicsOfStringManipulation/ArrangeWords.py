class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        lenn = 0
        for w in words:
            if len(w) > lenn:
                lenn = len(w)
        listA = [[] for i in range(lenn+1)]
        for w in words:
            listA[len(w)].append(w)
        aux = ''
        for z in listA:
            for c in z:
                aux += c+' '
        aux = aux[:len(aux)-1].capitalize()
        return aux
