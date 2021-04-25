class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        ans = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, right*2)
            elif right >= left:
                left = right = 0
        left = right = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, right*2)
            elif left >= right:
                left = right = 0
        return ans
