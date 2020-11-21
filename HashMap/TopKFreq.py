class Solution:
    def topKFrequent(self, nums, k: int):
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        listA = []
        for z in dic:
            listA.append((dic[z], z))
        listA.sort()
        ans = []
        for i in range(1, k+1):
            ans.append(listA[-i][1])
        return ans
