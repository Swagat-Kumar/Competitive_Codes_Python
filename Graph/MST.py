import heapq


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


pq = []
pq.append(Edge(3, 0, 3))
pq.append(Edge(3, 1, 5))
pq.append(Edge(3, 2, 3))
pq.append(Edge(1, 2, 2))
pq.append(Edge(4, 2, 7))
pq.append(Edge(4, 0, 12))
heapq.heapify(pq)


class UF:
    def __init__(self):
        self.id = {}
        self.sz = {}

    def root(self, v):
        if v not in self.id:
            self.id[v] = v
            self.sz[v] = 0
        while self.id[v] != v:
            self.id[v] = self.id[self.id[v]]
            v = self.id[v]
        return v

    def connected(self, v, w):
        return self.root(v) == self.root(w)

    def union(self, v, w):
        if v not in self.id:
            self.id[v] = v
            self.sz[v] = 0
        if w not in self.id:
            self.id[w] = w
            self.sz[w] = 0
        i = self.root(v)
        j = self.root(w)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
        elif self.sz[i] > self.sz[j]:
            self.id[j] = i
        else:
            self.id[j] = i
            self.sz[i] += 1


uf = UF()
count = 0
while len(pq) != 0 and count < 4:
    e = heapq.heappop(pq)
    if not uf.connected(e.v, e.w):
        uf.union(e.v, e.w)
        print(e)
        count += 1
