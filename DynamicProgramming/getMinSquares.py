# User function Template for python3
import math


class Solution:
    def MinSquares(self, nums):
        # Code here
        V = [nums]*(nums+1)
        for i in range(nums+1):
            if i <= 3:
                V[i] = i
                continue
            res = i
            for j in range(1, i+1):
                temp = j*j
                if temp > i:
                    break
                else:
                    res = min(res, 1+V[i-temp])
            V[i] = res
        return V[nums]
