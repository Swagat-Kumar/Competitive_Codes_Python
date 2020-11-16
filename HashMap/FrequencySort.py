class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        listc = []
        maxx = -1
        for c in s:
            if c not in dic:
                dic[c] = 1
                listc.append(c)
            else:
                dic[c] += 1
            if dic[c] > maxx:
                maxx = dic[c]
        ans = ''
        for j in range(maxx, 0, -1):
            aux = ''
            for k in dic:
                if dic[k] == j:
                    aux += k*j
            aux = ''.join(sorted(aux))
            ans += aux
        return ans
