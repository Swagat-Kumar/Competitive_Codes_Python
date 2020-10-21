class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        targetA = [-1]*len(nums)
        low = 0
        high = 0
        for i in range(len(nums)):
            ind = index[i]
            if ind >= low and ind <= high:
                for k in range(high, ind-1, -1):
                    try:
                        targetA[k+1] = targetA[k]
                    except:
                        pass
                targetA[ind] = nums[i]
            else:
                targetA[ind] = nums[i]
            high += 1
        return targetA
