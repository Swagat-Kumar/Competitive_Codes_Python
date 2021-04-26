class Solution:
    def isValidSudoku(self, board) -> bool:
        for r in range(len(board)):
            temp = []
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in temp:
                    return False
                temp.append(board[r][c])
        for c in range(len(board[0])):
            temp = []
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in temp:
                    return False
                temp.append(board[r][c])
        for rr in range(0, 9, 3):
            for cc in range(0, 9, 3):
                temp = []
                for r in range(3):
                    for c in range(3):
                        if board[r+rr][c+cc] == '.':
                            continue
                        if board[r+rr][c+cc] in temp:
                            return False
                        temp.append(board[r+rr][c+cc])
        return True
