class Solution:
    def updateBoard(self, board, click):
        revealed = [[False]*len(board[0]) for i in range(len(board))]

        def visit(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return
            if revealed[r][c]:
                return
            revealed[r][c] = True
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            mines = 0
            for rr in range(-1, 2):
                for cc in range(-1, 2):
                    if rr == 0 and cc == 0:
                        continue
                    if softVisit(r+rr, c+cc):
                        mines += 1
            if mines == 0:
                board[r][c] = 'B'
                for rr in range(-1, 2):
                    for cc in range(-1, 2):
                        visit(r+rr, c+cc)
            else:
                board[r][c] = str(mines)

        def softVisit(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
            return board[r][c] == 'M'
        visit(click[0], click[1])
        return board
