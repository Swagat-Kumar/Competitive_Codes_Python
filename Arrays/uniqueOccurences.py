class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for a in arr:
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
        listV = list(dic.values())
        listV.sort()
        for i in range(len(listV)-1):
            if listV[i] == listV[i+1]:
                return False
        return True
