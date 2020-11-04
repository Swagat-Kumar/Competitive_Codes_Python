class Solution:
    def frequencySort(self, nums):
        dic = {}
        listA = []
        for n in nums:
            if n not in dic:
                dic[n] = 1
                listA.append(n)
            else:
                dic[n] += 1
        aux = []
        for l in listA:
            aux.append((dic[l], -l))
        aux.sort()
        ans = []
        for a in aux:
            for i in range(a[0]):
                ans.append(-a[1])
        return ans
