class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        cumm = [0]*len(arr)
        cumm[0] = arr[0]
        for i in range(1, len(arr)):
            cumm[i] = cumm[i-1]+arr[i]
        sumA = 0
        for i in range(1, len(arr)+1, 2):
            start = 0
            while start+i-1 < len(arr):
                if start == 0:
                    sumA += cumm[start+i-1]
                    start += 1
                    continue
                sumA += cumm[start+i-1]-cumm[start-1]
                start += 1
        return sumA
