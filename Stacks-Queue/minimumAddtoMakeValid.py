class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        lb = 0
        count = 0
        for c in S:
            if c == '(':
                lb += 1
            elif c == ')':
                if lb == 0:
                    count += 1
                else:
                    lb -= 1
        return count+lb
