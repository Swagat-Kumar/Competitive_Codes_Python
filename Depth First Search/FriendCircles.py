class Solution:
    def findCircleNum(self, M) -> int:
        visited = [False]*len(M)

        def visit(current):
            if visited[current]:
                return
            visited[current] = True
            for i in range(len(M[0])):
                if M[current][i] == 1:
                    visit(i)
        count = 0
        for i in range(len(M)):
            if not visited[i]:
                visit(i)
                count += 1
        return count
