class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        def condition(a, b):
            return abs(ord(a)-ord(b)) == 32

        def solve(st):
            listA = []
            for c in st:
                if len(listA) == 0:
                    listA.append(c)
                    continue
                temp = listA.pop()
                if not condition(temp, c):
                    listA.append(temp)
                    listA.append(c)
            return ''.join(listA)

        aux = solve(s)
        while aux != s:
            s = aux
            aux = solve(s)
        return aux
