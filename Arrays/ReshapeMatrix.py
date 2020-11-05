class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        if r*c != len(nums)*len(nums[0]):
            return nums
        aux = [[-1]*c for i in range(r)]
        rr = 0
        cc = 0
        for n in nums:
            for e in n:
                aux[rr][cc] = e
                cc += 1
                if cc >= c:
                    rr += 1
                    cc = 0
        return aux
