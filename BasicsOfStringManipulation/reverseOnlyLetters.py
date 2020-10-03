class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        listS = list(S)
        start = 0
        end = len(listS)-1
        while start <= end:
            while (not listS[start].isalpha()) and start < end:
                start += 1
            while (not listS[end].isalpha()) and end > start:
                end -= 1
            if start <= end:
                listS[start], listS[end] = listS[end], listS[start]
            start += 1
            end -= 1
        return ''.join(listS)
