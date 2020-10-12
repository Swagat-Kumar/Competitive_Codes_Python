class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evenOut = []
        oddOut = []
        for i in range(len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                oddOut.append(i)
            elif i % 2 != 0 and A[i] % 2 == 0:
                evenOut.append(i)
        for j in range(len(evenOut)):
            A[evenOut[j]], A[oddOut[j]] = A[oddOut[j]], A[evenOut[j]]
        return A
