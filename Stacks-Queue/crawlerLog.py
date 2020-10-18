class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for l in logs:
            if l == '../':
                if depth > 0:
                    depth -= 1
            elif l == './':
                continue
            else:
                depth += 1
        return depth
