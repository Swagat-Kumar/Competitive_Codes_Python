class Solution:
    def subsets(self, nums):
        ans = []

        def solve(aux=[], curr=0):
            ans.append(list(aux))
            for i in range(curr, len(nums)):
                copy = list(aux)
                copy.append(nums[i])
                solve(copy, i+1)
        solve()
        return ans
