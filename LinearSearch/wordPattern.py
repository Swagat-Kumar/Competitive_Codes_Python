class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listS = list(s.split())
        if len(pattern) != len(listS):
            return False
        i = 0
        dicS = {}
        listedP = []
        for w in listS:
            if w not in dicS:
                if pattern[i] in listedP:
                    return False
                dicS[w] = pattern[i]
                listedP.append(pattern[i])
            else:
                if dicS[w] != pattern[i]:
                    return False
            i += 1
        return True
