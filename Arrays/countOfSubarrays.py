class Solution:
    def countSubarray(self, arr, n, k):
        count = 0
        listL = []
        for i in range(n):
            if arr[i] > k:
                count += (n-i)
                count += (n-i)*len(listL)
                listL = []
            else:
                listL.append(i)
        return count
