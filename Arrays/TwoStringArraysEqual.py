class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        wordd = ''
        worde = ''
        for w in word1:
            wordd += w
        for w in word2:
            worde += w
        return wordd == worde
