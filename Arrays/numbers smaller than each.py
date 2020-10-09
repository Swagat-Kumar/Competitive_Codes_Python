class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        aux = [0]*101
        for n in nums:
            aux[n] += 1
        for i in range(1, 101):
            aux[i] += aux[i-1]
        ans = []
        for n in nums:
            if n == 0:
                ans.append(0)
                continue
            ans.append(aux[n-1])
        return ans
