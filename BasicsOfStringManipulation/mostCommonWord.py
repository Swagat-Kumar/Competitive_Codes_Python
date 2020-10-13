class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        aux = paragraph.lower()
        word = ''
        words = []
        for p in aux:
            if ord(p) > 96 and ord(p) < 133:
                word += p
            else:
                if word != '' and word not in banned:
                    words.append(word)
                word = ''
        if word != '' and word not in banned:
            words.append(word)
        for w in words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        maxx = -1
        key = ''
        for w in list(dic.keys()):
            if dic[w] > maxx:
                maxx = dic[w]
                key = w
        return key
