class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        aux = [-1]*len(arr)
        a = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            aux[i] = a
            if arr[i] > a:
                a = arr[i]
        return aux
