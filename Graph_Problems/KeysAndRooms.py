class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [-1]*len(rooms)

        def visit(pos):
            visited[pos] = 0
            for k in rooms[pos]:
                if visited[k] == 0:
                    continue
                if visited[k] == -1:
                    visit(k)
            visited[pos] = 1
        visit(0)
        for v in visited:
            if v != 1:
                return False
        return True
