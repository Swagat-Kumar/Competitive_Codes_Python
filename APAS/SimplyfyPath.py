class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        ans = '/'
        stack = []
        for p in paths:
            if len(p) == 0:
                continue
            if p == '..':
                if len(stack) != 0:
                    stack.pop()
            elif p == '.':
                continue
            else:
                stack.append(p)
        ans += '/'.join(stack)
        return ans
