class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xorGate(a, b):
            return a ^ b
        if n == 1:
            return start
        ans = xorGate(start, start+2)
        i = 2
        while i < n:
            num = start+2*i
            ans = xorGate(num, ans)
            i += 1
        return ans
