class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y[0] == '-':
            return False
        return int(y[::-1]) == x
