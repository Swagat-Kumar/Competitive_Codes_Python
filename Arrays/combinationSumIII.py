class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        ans = []

        def recurr(listA=[], curr=0):
            if len(listA) == k:
                if sum(listA) == n:
                    ans.append(listA)
                return
            for i in range(curr+1, 10):
                cA = list(listA)
                if i not in cA:
                    cA.append(i)
                    recurr(cA, i)
        recurr()
        return ans
