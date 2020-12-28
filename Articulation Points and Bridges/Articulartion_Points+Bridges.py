class Graph:
    def __init__(self, vertices):
        self.adj = [[] for i in range(vertices)]
        self.vertices = vertices
        self.edges = 0

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.edges += 1

    def adjacent(self, v):
        return self.adj[v]

    def countEdges(self):
        return self.edges

    def countVertices(self):
        return self.vertices


class Articulation_Points:
    def __init__(self, myGraph, source):
        self.visited = [False]*myGraph.countVertices()
        self.discoveryTime = [-1]*myGraph.countVertices()
        self.low = [-1]*myGraph.countVertices()
        self.parent = [-1]*myGraph.countVertices()
        self.ap = [False]*myGraph.countVertices()
        self.vertices = myGraph.countVertices()
        self.bridgeList = []
        self.time = 0
        self.dfs(myGraph, source)

    def dfs(self, myGraph, vertex):
        self.visited[vertex] = True
        self.discoveryTime[vertex] = self.time+1
        self.low[vertex] = self.time+1
        child = 0
        for v in myGraph.adjacent(vertex):
            if not self.visited[v]:
                child += 1
                self.parent[v] = vertex
                self.time += 1
                self.dfs(myGraph, v)
                self.low[vertex] = min(self.low[vertex], self.low[v])
                if self.parent[vertex] == -1 and child > 1:
                    self.ap[vertex] = True
                if self.parent[vertex] != -1 and self.low[v] >= self.discoveryTime[vertex]:
                    self.ap[vertex] = True
                if self.low[v] > self.discoveryTime[vertex]:
                    if (vertex, v) not in self.bridgeList:
                        self.bridgeList.append((vertex, v))
            elif self.parent[vertex] != v:
                self.low[vertex] = min(self.low[vertex], self.discoveryTime[v])

    def discovery(self):
        for i in range(self.vertices):
            print(i, ' = ', self.discoveryTime[i])

    def points(self):
        count = 0
        listP = []
        for i in range(self.vertices):
            if self.ap[i]:
                count += 1
                listP.append(i)
        print(count)
        for p in listP:
            print(p, end=' ')
        print()

    def bridges(self):
        print(len(self.bridgeList))
        self.bridgeList.sort()
        for b in self.bridgeList:
            print(b[0], b[1])


n, m = map(int, input().split())
myGraph = Graph(n)
for i in range(m):
    a, b = map(int, input().split())
    myGraph.addEdge(a, b)
ap = Articulation_Points(myGraph, 0)
ap.points()
ap.bridges()
