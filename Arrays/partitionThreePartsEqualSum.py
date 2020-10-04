class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        eachSum = total/3
        i = 0
        j = -1
        sumA = 0
        for x in range(len(A)):
            sumA += A[x]
            if sumA == eachSum:
                i = x
                break
        sumA = 0
        for x in range(i+1, len(A)):
            sumA += A[x]
            if sumA == eachSum:
                j = x+1
                break
        if j >= len(A) or j == -1:
            return False
        if i+1 < j:
            return True
        else:
            return False
