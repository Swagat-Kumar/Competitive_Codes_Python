class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for p in paths:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])
        alloted = [-1]*(n+1)
        for i in range(1, n+1):
            found = []
            for adj in graph[i]:
                if alloted[adj] != -1:
                    found.append(alloted[adj])
            for k in range(1, 5):
                if k not in found:
                    alloted[i] = k
                    break
        alloted.pop(0)
        return alloted
