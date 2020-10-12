class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def ssort(st):
            even = []
            odd = []
            for i in range(len(st)):
                if i % 2 == 0:
                    even.append(st[i])
                else:
                    odd.append(st[i])
            even.sort()
            e = 0
            odd.sort()
            o = 0
            aux = ''
            for i in range(len(st)):
                if i % 2 == 0:
                    aux += even[e]
                    e += 1
                else:
                    aux += odd[o]
                    o += 1
            return aux
        dic = {}
        for a in A:
            aux = ssort(a)
            if aux not in dic:
                dic[aux] = 1
            else:
                dic[aux] += 1
        return len(dic.keys())
