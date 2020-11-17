class Solution:
    def minStartValue(self, nums) -> int:
        minn = 10*6
        aux = 0
        for n in nums:
            aux += n
            if aux < minn:
                minn = aux
        if minn >= 1:
            return 1
        return abs(minn)+1
