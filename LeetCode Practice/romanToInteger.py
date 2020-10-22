class Solution:
    def romanToInt(self, s: str) -> int:
        hi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        current = ''
        for i in range(len(s)-1):
            if hi[s[i]] < hi[s[i+1]]:
                ans += -1*hi[s[i]]
            else:
                ans += hi[s[i]]
        ans += hi[s[len(s)-1]]
        return ans
