class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        return True
