class Solution:
    def trimMean(self, arr) -> float:
        arr.sort()
        n = len(arr)
        total = sum(arr)
        five = (n*5)//100
        for i in range(five):
            total -= arr[i]
            n -= 1
        for j in range(len(arr)-1, len(arr)-1-five, -1):
            total -= arr[j]
            n -= 1
        return total/n
