n, m = map(int, input().split())
graph = {}
ans = []
for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    if b not in graph[a]:
        graph[a] += [b]
    if a not in graph[b]:
        graph[b] += [a]
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    if a not in graph:
        ans.append("NO")
        continue

    if b in graph[a]:
        ans.append("YES")
        continue
    else:
        ans.append("NO")
for a in ans:
    print(a)
