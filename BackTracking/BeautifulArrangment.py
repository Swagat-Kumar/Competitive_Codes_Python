class Solution:
    def countArrangement(self, N: int) -> int:
        aux = []
        for i in range(1, N+1):
            count = []
            for n in range(1, N+1):
                if n % i == 0 or i % n == 0:
                    count.append(n)
            aux.append(count)
        self.ans = 0

        def visit(current=0, listA=[]):
            if current == len(aux):
                self.ans += 1
                return
            for a in aux[current]:
                copy = list(listA)
                if a not in copy:
                    copy.append(a)
                    visit(current+1, copy)
        visit()
        return self.ans
