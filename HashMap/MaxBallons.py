class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        listA = [0]*26
        for t in text:
            listA[ord(t)-97] += 1
        minn = 10**4
        for c in 'balon':
            if c == 'l' or c == 'o':
                if listA[ord(c)-97]//2 < minn:
                    minn = listA[ord(c)-97]//2
            else:
                if listA[ord(c)-97] < minn:
                    minn = listA[ord(c)-97]
        return minn
