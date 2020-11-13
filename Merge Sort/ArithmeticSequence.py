class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def isArithmetic(low, high):
            listA = nums[low:high+1]
            listA.sort()
            diff = listA[1]-listA[0]
            for i in range(2, len(listA)):
                if listA[i]-listA[i-1] != diff:
                    return False
            return True
        ans = []
        for i in range(len(l)):
            ans.append(isArithmetic(l[i], r[i]))
        return ans
