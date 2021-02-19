class Solution:
    def shiftPile(self, N, n):
        # code here
        self.step = 0
        ans = ['0', '0']

        def move(N, start, using, end):
            if N < 1:
                return
            move(N-1, start, end, using)
            self.step += 1
            if self.step == n:
                ans[0] = start
                ans[1] = end
            move(N-1, using, start, end)
        move(N, '1', '2', '3')
        return ans
