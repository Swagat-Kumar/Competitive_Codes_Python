class Solution:
    def sortString(self, s: str) -> str:
        nChars = 0
        chars = [0]*26
        for c in s:
            chars[ord(c)-97] += 1
        forward = True
        ans = ''
        while len(ans) < len(s):
            if forward:
                for i in range(26):
                    if chars[i] > 0:
                        chars[i] -= 1
                        ans += chr(i+97)
                forward = False
            else:
                for i in range(25, -1, -1):
                    if chars[i] > 0:
                        chars[i] -= 1
                        ans += chr(i+97)
                forward = True
        return ans
