class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        listA = []
        xP = 0
        yP = n
        for i in range(2*n):
            if i % 2 == 0:
                listA.append(nums[xP])
                xP += 1
            else:
                listA.append(nums[yP])
                yP += 1
        return listA
