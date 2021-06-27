class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []

        def solver(aux=[], curr=0):
            ans.append(list(aux))
            for i in range(curr, len(nums)):
                if i != curr and nums[i-1] == nums[i]:
                    continue
                aux.append(nums[i])
                solver(aux, i+1)
                aux.pop()
        solver()
        return ans
# my way
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans = []

#         def solve(aux=[], curr=0):
#             if curr == len(nums):
#                 if aux not in ans:
#                     ans.append(aux)
#                 return
#             copy = list(aux)
#             solve(copy, curr+1)
#             copy = list(aux)
#             copy.append(nums[curr])
#             solve(copy, curr+1)
#         solve()
#         return ans
