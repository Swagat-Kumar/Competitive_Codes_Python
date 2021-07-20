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


class DiGraph:
    def __init__(self) -> None:
        self.conections = {}
        self.vertices = 0
        self.edges = 0

    def addEdge(self, edge):
        if edge.v not in self.conections:
            self.conections[edge.v] = []
            self.vertices += 1
        if edge.w not in self.conections:
            self.conections[edge.w] = []
            self.vertices += 1
        self.conections[edge.v].append(edge)
        self.edges += 1

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
            print(a, ':', list(map(str, self.conections[a])))
