class Solution:
    def pivotIndex(self, nums) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        def sumAux(nos):
            if len(nos) < 1:
                return []
            aux = [0]*len(nos)
            aux[0] = nos[0]
            for i in range(1, len(nos)):
                aux[i] = aux[i-1]+nos[i]
            return aux
        fSum = sumAux(nums)
        bSum = sumAux(nums[::-1])[::-1]
        if bSum[1] == 0:
            return 0
        for i in range(1, len(nums)-1):
            if fSum[i-1] == bSum[i+1]:
                return i
        if fSum[-2] == 0:
            return len(nums)-1
        return -1
