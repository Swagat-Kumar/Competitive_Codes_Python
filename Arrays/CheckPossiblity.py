class Solution:
    def checkPossibility(self, nums) -> bool:
        def check(listA):
            for i in range(len(listA)-1):
                if listA[i+1] < listA[i]:
                    return False
            return True
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                listA = list(nums)
                listA[i] = listA[i+1]
                listB = list(nums)
                listB[i+1] = listB[i]
                if not check(listA) and not check(listB):
                    return False
        return True
