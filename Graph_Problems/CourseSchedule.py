class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for p in prerequisites:
            graph[p[0]].append(p[1])
        visited = [-1]*numCourses

        def visit(pos):
            visited[pos] = 0
            others = True
            for adj in graph[pos]:
                if visited[adj] == 0:
                    return False
                if visited[adj] == -1:
                    if not visit(adj):
                        others = False
                        break
            visited[pos] = 1
            return others
        complete = True
        for i in range(numCourses):
            visited = [-1]*numCourses
            if not visit(i):
                complete = False
        return complete
