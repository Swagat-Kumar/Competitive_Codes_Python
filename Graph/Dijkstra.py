import heapq


class Edge:
    def __init__(self, v, w, weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    def __eq__(self, o: object) -> bool:
        if o == None:
            return NotImplemented
        return self.weight == o.weight

    def __lt__(self, o):
        if o == None:
            return NotImplemented
        return self.weight < o.weight


class Graph:
    def __init__(self) -> None:
        self.connections = {}

    def addEdge(self, v, w, weight):
        if v not in self.connections:
            self.connections[v] = []
        self.connections[v].append(Edge(v, w, weight))

    def adjacent(self, v):
        if v not in self.connections:
            return []
        else:
            return self.connections[v]


myGraph = Graph()
myGraph.addEdge(0, 1, 5)
myGraph.addEdge(0, 4, 9)
myGraph.addEdge(0, 7, 8)
myGraph.addEdge(1, 2, 12)
myGraph.addEdge(1, 3, 15)
myGraph.addEdge(1, 7, 4)
myGraph.addEdge(2, 3, 3)
myGraph.addEdge(2, 6, 11)
myGraph.addEdge(3, 6, 9)
myGraph.addEdge(4, 5, 4)
myGraph.addEdge(4, 6, 20)
myGraph.addEdge(4, 7, 5)
myGraph.addEdge(5, 2, 1)
myGraph.addEdge(5, 6, 13)
myGraph.addEdge(7, 5, 6)
myGraph.addEdge(7, 2, 7)

print(myGraph.connections)
disTo = {}
edgeTo = {}
pq = []
pq.append((0, 0))
disTo[0] = 0
while len(pq) != 0:
    vertex = heapq.heappop(pq)
    for edge in myGraph.adjacent(vertex[1]):
        v = edge.v
        w = edge.w
        if v not in disTo:
            disTo[v] = 10**9
        if w not in disTo:
            disTo[w] = 10**9
        if disTo[w] > disTo[v]+edge.weight:
            edgeTo[w] = v
            if pq.count((disTo[w], w)):
                pq.remove((disTo[w], w))
                disTo[w] = disTo[v]+edge.weight
                pq.append((disTo[w], w))
                heapq.heapify(pq)
            else:
                disTo[w] = disTo[v]+edge.weight
                heapq.heappush(pq, (disTo[w], w))
print(disTo)
print(edgeTo)
