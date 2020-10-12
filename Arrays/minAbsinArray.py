class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minAb = 10**8
        arr.sort()
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) < minAb:
                minAb = abs(arr[i]-arr[i-1])
        listA = []
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) == minAb:
                listA.append([arr[i-1], arr[i]])
        return listA
