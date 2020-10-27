class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ways = []

        def waysTo(current, listA=[]):
            if current == len(graph)-1:
                ways.append(listA)
            listA.append(current)
            for adj in graph[current]:
                copy = list(listA)
                waysTo(adj, copy)
        waysTo(0)
        return ways
