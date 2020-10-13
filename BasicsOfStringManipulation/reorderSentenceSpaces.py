class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        word = ''
        spaceCount = 0
        for p in text:
            if ord(p) > 96 and ord(p) < 133:
                word += p
            else:
                spaceCount += 1
                if word != '':
                    words.append(word)
                word = ''
        if word != '':
            words.append(word)
        if len(words) == 1:
            return words[0]+' '*spaceCount
        sn = spaceCount//(len(words)-1)
        ex = spaceCount % (len(words)-1)
        aux = ''
        for w in words:
            aux += w+sn*' '
        aux = aux[:len(aux)-sn]
        aux += ' '*ex
        return aux
