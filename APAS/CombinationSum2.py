class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        ans = []
        self.total = sum(candidates)

        def recurr(aux=[0], i=0):
            summ = sum(aux)
            if summ >= target or self.total < target:
                if summ == target:
                    if aux[1:] not in ans:
                        ans.append(aux[1:])
                return
            for j in range(i, len(candidates)):
                if summ+candidates[j] <= target:
                    copy = list(aux)
                    copy.append(candidates[j])
                    recurr(copy, j+1)
                else:
                    break
                while j < len(candidates)-1 and candidates[j] == candidates[j+1]:
                    j += 1
        recurr()
        return ans
