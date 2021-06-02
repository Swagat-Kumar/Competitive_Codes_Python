class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def solve(aux=[], curr=1):
            if len(aux) == k:
                ans.append(list(aux))
                return
            for i in range(curr, n+1):
                copy = list(aux)
                copy.append(i)
                solve(copy, i+1)
        solve()
        return ans
