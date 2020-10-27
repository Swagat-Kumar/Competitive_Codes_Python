class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        def addEdge(a, b):
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)
        for r in roads:
            addEdge(r[0], r[1])
            addEdge(r[1], r[0])
        maxN = 0
        for i in range(n-1):
            for j in range(i+1, n):
                va = i
                vb = j
                count = 0
                if len(graph[va])+len(graph[vb]) < maxN:
                    continue
                for e in graph[va]:
                    if e == vb:
                        continue
                    count += 1
                for e in graph[vb]:
                    if e == va:
                        continue
                    count += 1
                if vb in graph[va]:
                    count += 1
                if count > maxN:
                    maxN = count
        return maxN
