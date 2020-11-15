class Solution:
    def minOperations(self, n: int) -> int:
        start = 1
        end = 2*(n-1)+1
        ans = 0
        while start < end:
            ans += (end-start)//2
            start += 2
            end -= 2
        return ans
