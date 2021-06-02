class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""
        dt = {}
        for c in t:
            if c not in dt:
                dt[c] = 1
            else:
                dt[c] += 1
        required = len(dt)
        left = 0
        right = 0
        formed = 0
        ds = {}
        ans = ""
        ansLen = len(s)
        while right < len(s):
            c = s[right]
            if c not in ds:
                ds[c] = 1
            else:
                ds[c] += 1
            if c in dt and ds[c] == dt[c]:
                formed += 1
            while left <= right and formed == required:
                c = s[left]
                aux = s[left:right+1]
                if len(aux) <= ansLen:
                    ans = aux
                    ansLen = len(aux)
                ds[c] -= 1
                if c in dt and ds[c] < dt[c]:
                    formed -= 1
                left += 1
            right += 1
        return ans
