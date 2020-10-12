class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        while end > start:
            s[end], s[start] = s[start], s[end]
            end -= 1
            start += 1
        return s
