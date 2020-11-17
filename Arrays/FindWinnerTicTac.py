class Solution:
    def tictactoe(self, moves) -> str:
        grid = [[' ']*3 for i in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                grid[moves[i][0]][moves[i][1]] = 'X'
            else:
                grid[moves[i][0]][moves[i][1]] = 'O'
        for r in range(3):
            win = True
            winner = grid[r][0]
            if winner == ' ':
                continue
            for c in range(2):
                if grid[r][c] != grid[r][c+1]:
                    win = False
                    break
            if win:
                if winner == 'X':
                    return 'A'
                else:
                    return 'B'
        for c in range(3):
            winner = grid[0][c]
            win = True
            if winner == ' ':
                continue
            for r in range(2):
                if grid[r+1][c] != grid[r][c]:
                    win = False
                    break
            if win:
                if winner == 'X':
                    return 'A'
                else:
                    return 'B'
        winner = grid[0][0]
        if winner != ' ':
            win = True
            for i in range(2):
                if grid[i][i] != grid[i+1][i+1]:
                    win = False
                    break
            if win:
                if winner == 'X':
                    return 'A'
                else:
                    return 'B'
        winner = grid[0][2]
        if winner != ' ':
            if winner == grid[1][1] == grid[2][0]:
                if winner == 'X':
                    return 'A'
                else:
                    return 'B'
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
