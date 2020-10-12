class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countL = [0]*26
        for c in chars:
            countL[ord(c)-ord('a')] += 1

        def check(word, listL):
            for l in word:
                if listL[ord(l)-ord('a')] == 0:
                    return False
                listL[ord(l)-ord('a')] -= 1
            return True
        ans = 0
        for w in words:
            if check(w, list(countL)):
                ans += len(w)
        return ans
