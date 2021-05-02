class Solution:
    def permute(self, nums):
        ans = []

        def resolve(a, step=0):
            if step == len(a):
                ans.append(a)
                return
            for i in range(step, len(a)):
                copy = list(a)
                copy[i], copy[step] = copy[step], copy[i]
                resolve(copy, step+1)
        resolve(nums)
        return ans
