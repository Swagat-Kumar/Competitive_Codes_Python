class Solution:
    def groupThePeople(self, groupSizes):
        dic = {}
        ans = []
        for i in range(len(groupSizes)):
            x = groupSizes[i]
            if x not in dic:
                dic[x] = [i]
            else:
                dic[x].append(i)
            if len(dic[x]) == x:
                ans.append(dic[x])
                dic[x] = []
        return ans
