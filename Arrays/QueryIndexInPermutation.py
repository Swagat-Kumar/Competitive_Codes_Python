class Solution:
    def processQueries(self, queries, m: int):
        P = [x for x in range(1, m+1)]

        def linearSearch(x):
            for i in range(len(P)):
                if P[i] == x:
                    return i
        ans = []
        for q in queries:
            poss = linearSearch(q)
            ans.append(poss)
            del P[poss]
            P.insert(0, q)
        return ans
