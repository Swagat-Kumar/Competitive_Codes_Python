class Solution:
    def longestPalindrome(self, s: str) -> int:
        small = [0]*26
        capital = [0]*26
        for c in s:
            if ord(c) >= 97 and ord(c) <= 122:
                small[ord(c)-97] += 1
            else:
                capital[ord(c)-65] += 1
        evenC = 0
        oddC = 0
        for s in small:
            if s % 2 == 0:
                evenC += s
            else:
                evenC += s-1
                oddC = 1
        for s in capital:
            if s % 2 == 0:
                evenC += s
            else:
                evenC += s-1
                oddC = 1
        return evenC+oddC
