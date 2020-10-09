class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cr = 0
        cl = 0
        count = 0
        for l in s:
            if l == 'R':
                cr += 1
            elif l == 'L':
                cl += 1
            else:
                continue
            if cr == cl:
                count += 1
        return count
