class Solution:

    def valueEqualToIndex(self, arr, n):
        # code here
        self.count = []
        for i in range(len(arr)):
            if arr[i] == i+1:
                self.count.append(i+1)
        return self.count
