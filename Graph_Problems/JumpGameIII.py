class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper
        visited = [False]*len(arr)

        def visit(pos):
            if pos < 0 or pos >= len(arr):
                return False
            if visited[pos]:
                return False
            visited[pos] = True
            if arr[pos] == 0:
                return True
            return visit(pos+arr[pos]) or visit(pos-arr[pos])
        visit = memoize(visit)
        return visit(start)
