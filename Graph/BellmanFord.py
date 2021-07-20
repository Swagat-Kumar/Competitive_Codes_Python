class Edge:
    def __init__(self, v, w, weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    def __eq__(self, other) -> bool:
        if other == None:
            return NotImplemented
        return self.weight == other.weight

    def __lt__(self, other):
        if other == None:
            return NotImplemented
        return self.weight < other.weight

    def __str__(self) -> str:
        return f'{self.v}-{self.weight}-{self.w}'


edges = []
dis = {}
edgeTO = {}
edges.append(Edge(0, 1, 1))
edges.append(Edge(0, 2, 4))
edges.append(Edge(1, 2, -2))
edges.append(Edge(1, 3, 2))
edges.append(Edge(1, 4, 7))
edges.append(Edge(2, 3, 3))
edges.append(Edge(3, 4, 4))
edges.append(Edge(4, 5, 7))
edges.append(Edge(5, 3, -3))
dis[0] = 0
for i in edges:
    for e in edges:
        if e.v not in dis:
            dis[e.v] = 10**9
        if e.w not in dis:
            dis[e.w] = 10**9
        if dis[e.v]+e.weight < dis[e.w]:
            dis[e.w] = dis[e.v]+e.weight
            edgeTO[e.w] = e.v
print(edgeTO)
