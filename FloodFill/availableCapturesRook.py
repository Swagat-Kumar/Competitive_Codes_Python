class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0

        def visit(x, y):
            if board[x][y] == 'p':
                return 1
            elif board[x][y] == '.':
                return 0
            else:
                return -1
        r = 0
        c = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    r = i
                    c = j
                    break
        for rr in range(r+1, len(board)):
            if visit(rr, c) == 1:
                ans += 1
                break
            if visit(rr, c) == 0:
                continue
            else:
                break
        for rr in range(r-1, -1, -1):
            if visit(rr, c) == 1:
                ans += 1
                break
            if visit(rr, c) == 0:
                continue
            else:
                break
        for cc in range(c+1, len(board[0])):
            if visit(r, cc) == 1:
                ans += 1
                break
            if visit(r, cc) == 0:
                continue
            else:
                break
        for cc in range(c-1, -1, -1):
            if visit(r, cc) == 1:
                ans += 1
                break
            if visit(r, cc) == 0:
                continue
            else:
                break
        return ans
