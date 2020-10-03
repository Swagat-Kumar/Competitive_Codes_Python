def dfs(visited, matrix, x, y):
    if x == n-1 and y == m-1:
        return True
    if x < 0 or x > m-1:
        return False
    if y < 0 or y > n-1:
        return False
    if matrix[x][y] == 1:
        if visited[x][y]:
            return False
        visited[x][y] = True
        if(dfs(visited, matrix, x-1, y)):
            return True
        if(dfs(visited, matrix, x+1, y)):
            return True
        if(dfs(visited, matrix, x, y-1)):
            return True
        if(dfs(visited, matrix, x, y+1)):
            return True
    return False


n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
visited = [[False for i in range(m)] for j in range(n)]
if dfs(visited, matrix, 0, 0):
    print('Yes')
else:
    print('No')
