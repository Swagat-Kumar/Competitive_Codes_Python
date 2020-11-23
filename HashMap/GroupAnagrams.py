class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            aux = ''.join(sorted(s))
            if aux not in dic:
                dic[aux] = [s]
            else:
                dic[aux].append(s)
        ans = []
        for d in dic:
            ans.append(dic[d])
        return ans
