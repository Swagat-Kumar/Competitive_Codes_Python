class Solution:
    def reverseVowels(self, s: str) -> str:
        listA = list(s)
        start = 0
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        end = len(listA)-1
        while start < end:
            while listA[start] not in vowel:
                start += 1
                if start >= len(listA):
                    break
            while listA[end] not in vowel:
                end -= 1
                if end < 0:
                    break
            if start < end:
                listA[start], listA[end] = listA[end], listA[start]
            start += 1
            end -= 1
        return ''.join(listA)
