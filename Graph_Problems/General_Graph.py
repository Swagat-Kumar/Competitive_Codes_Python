class Graph:
    def __init__(self, graph=None):
        if graph is None:
            graph = {}
        self.graph = graph
        self.vCount = 0
        self.eCount = 0

    def V(self):
        return self.vCount

    def E(self):
        return self.eCount

    def isVertex(self, vertex):
        if vertex not in self.graph:
            return False
        return True

    def adjacent(self, vertex):
        if vertex not in self.graph:
            return None
        return list(self.graph[vertex])

    def getVertices(self):
        return list(self.graph.keys())

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            self.vCount += 1

    def addEdge(self, v, w):
        self.eCount += 1
        if v not in self.graph:
            self.graph[v] = [w]
            self.vCount += 1
        else:
            self.graph[v].append(w)
        if w not in self.graph:
            self.graph[w] = [v]
            self.vCount += 1
        else:
            self.graph[w].append(v)
