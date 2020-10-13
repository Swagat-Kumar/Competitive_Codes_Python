class Solution:
    def isPalindrome(self, s: str) -> bool:
        aux = s.lower()
        ref = ''
        for a in aux:
            if ord(a) > 96 and ord(a) < 123:
                ref += a
            if ord(a) > 47 and ord(a) < 58:
                ref += a
        if ref == ref[::-1]:
            return True
        else:
            return False
