class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = {}
        for i in range(1, N+1):
            graph[i] = []
        person = []

        def addTrust(a, b):
            graph[a].append(b)
        for t in trust:
            addTrust(t[0], t[1])
        ans = -1
        for j in range(1, N+1):
            if len(graph[j]) == 0:
                found = True
                for i in range(1, N+1):
                    if i == j:
                        continue
                    if j not in graph[i]:
                        found = False
                if found:
                    ans = j
                    break
        return ans
