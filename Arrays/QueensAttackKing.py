class Solution:
    def queensAttacktheKing(self, queens, king):
        board = [[False]*8 for i in range(8)]
        for q in queens:
            board[q[0]][q[1]] = True

        def visit(r, c):
            if r < 0 or c < 0 or r >= 8 or c >= 8:
                return None
            if board[r][c]:
                return True
            else:
                return False
        ans = []
        for r in range(1, 7):
            z = visit(king[0]+r, king[1])
            if z == None:
                break
            if z:
                ans.append([king[0]+r, king[1]])
                break
        for r in range(1, 7):
            z = visit(king[0]-r, king[1])
            if z == None:
                break
            if z:
                ans.append([king[0]-r, king[1]])
                break
        for c in range(1, 7):
            z = visit(king[0], king[1]+c)
            if z == None:
                break
            if z:
                ans.append([king[0], king[1]+c])
                break
        for c in range(1, 7):
            z = visit(king[0], king[1]-c)
            if z == None:
                break
            if z:
                ans.append([king[0], king[1]-c])
                break
        for i in range(1, 7):
            z = visit(king[0]+i, king[1]+i)
            if z == None:
                break
            if z:
                ans.append([king[0]+i, king[1]+i])
                break
        for i in range(1, 7):
            z = visit(king[0]-i, king[1]-i)
            if z == None:
                break
            if z:
                ans.append([king[0]-i, king[1]-i])
                break
        for i in range(1, 7):
            z = visit(king[0]+i, king[1]-i)
            if z == None:
                break
            if z:
                ans.append([king[0]+i, king[1]-i])
                break
        for i in range(1, 7):
            z = visit(king[0]-i, king[1]+i)
            if z == None:
                break
            if z:
                ans.append([king[0]-i, king[1]+i])
                break
        return ans
