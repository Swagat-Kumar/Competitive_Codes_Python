class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort(aux, low, high):
            for i in range(low, high+1):
                minnI = i
                for j in range(i, high+1):
                    if aux[j] < aux[minnI]:
                        minnI = j
                aux[i], aux[minnI] = aux[minnI], aux[i]
        found = False
        spot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                found = True
                spot = i
                break
        if not found:
            sort(nums, 0, len(nums)-1)
        else:
            minn = spot
            maxx = 2**31
            for j in range(spot+1, len(nums)):
                if nums[j] > nums[spot] and nums[j] <= maxx:
                    minn = j
                    maxx = nums[j]
            nums[minn], nums[spot] = nums[spot], nums[minn]
            sort(nums, spot+1, len(nums)-1)
