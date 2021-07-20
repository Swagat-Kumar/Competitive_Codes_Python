import heapq
adj = {}
n, m = map(int, input().split())
for i in range(m):
    a, b, w = map(int, input().split())
    if a not in adj:
        adj[a] = []
    if b not in adj:
        adj[b] = []
    adj[a].append((b, w))
dist = {}
dist[1] = 0
pq = []
pq.append((0, 1))
while len(pq) != 0:
    v = heapq.heappop(pq)
    v = v[1]
    for a in adj[v]:
        w = a[0]
        weight = a[1]
        if w not in dist:
            dist[w] = 10**9
        if v not in dist:
            dist[v] = 10**9
        if dist[w] > dist[v]+weight:
            small = dist[v]+weight
            if pq.count((dist[w], w)):
                pq.remove((dist[w], w))
                dist[w] = small
                pq.append((small, w))
                heapq.heapify(pq)
            else:
                dist[w] = small
                heapq.heappush(pq, (small, w))
print(dist)
