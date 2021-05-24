import numpy as np


class Solution:
    def solveNQueens(self, n: int):
        ans = []

        def solve(arr=[['.']*n for i in range(n)], row=0, count=0, rm=[False]*n, cm=[False]*n, ltr=[False]*(2*n-1), rtl=[False]*(2*n-1)):
            if count == n:
                copy = []
                for a in arr:
                    copy.append(''.join(a))
                if copy not in ans:
                    ans.append(copy)
                return
            for r in range(row, n):
                for c in range(n):
                    if not ltr[r+c] and not rtl[abs(n-1-r)+c] and not rm[r] and not cm[c]:
                        arr[r][c] = 'Q'
                        ltr[r+c] = True
                        rtl[abs(n-1-r)+c] = True
                        rm[r] = True
                        cm[c] = True
                        solve(arr, r+1, count+1, rm, cm, ltr, rtl)
                        arr[r][c] = '.'
                        ltr[r+c] = False
                        rtl[abs(n-1-r)+c] = False
                        rm[r] = False
                        cm[c] = False

        solve()
        for a in ans:
            print(np.matrix(a))
        return ans
