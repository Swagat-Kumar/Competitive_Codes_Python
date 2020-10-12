class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = [False]*len(arr)
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                odds[i] = True
        for i in range(1, len(arr)-1):
            if odds[i] and odds[i-1] and odds[i+1]:
                return True
        return False
