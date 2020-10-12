class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        remainder = []
        for a in arr2:
            dic[a] = 0
        for a in arr1:
            if a not in dic:
                remainder.append(a)
            else:
                dic[a] += 1
        remainder.sort()
        i = 0
        for a in arr2:
            for j in range(dic[a]):
                arr1[i] = a
                i += 1
        for r in remainder:
            arr1[i] = r
            i += 1
        return arr1
