class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        start = 0
        ans = []
        while start < len(nums)-1:
            freq = nums[start]
            for i in range(freq):
                ans.append(nums[start+1])
            start += 2
        return ans
