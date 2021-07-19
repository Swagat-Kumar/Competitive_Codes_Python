class Graph:
    def __init__(self) -> None:
        self.conections = {}
        self.vertices = 0
        self.edges = 0

    def addEdge(self, v, w):
        if v not in self.conections:
            self.conections[v] = []
            self.vertices += 1
        if w not in self.conections:
            self.conections[w] = []
            self.vertices += 1
        self.conections[v].append(w)
        self.edges += 1
        self.conections[w].append(v)

    def adjacent(self, v):
        if v not in self.conections:
            return []
        else:
            return self.conections[v]

    def V(self):
        return self.vertices

    def E(self):
        return self.edges

    def toString(self):
        for a in self.conections:
            print(a, self.conections[a])


myGraph = Graph()

myGraph.addEdge(0, 1)
myGraph.addEdge(0, 2)
myGraph.addEdge(0, 5)
myGraph.addEdge(0, 6)
myGraph.addEdge(3, 4)
myGraph.addEdge(3, 5)
myGraph.addEdge(4, 5)
myGraph.addEdge(4, 6)
myGraph.addEdge(7, 8)


def dfs(graph, source, marked={}):
    marked[source] = True
    for a in graph.adjacent(source):
        if a not in marked:
            marked[a] = False
        if not marked[a]:
            dfs(graph, a, marked)
            print(a)


dfs(myGraph, 0)
