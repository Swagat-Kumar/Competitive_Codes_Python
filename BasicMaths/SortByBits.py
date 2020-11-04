class Solution:
    def sortByBits(self, arr):
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        def num1(n):
            if n < 2:
                return n
            if n % 2 == 0:
                return num1(n/2)
            else:
                return 1+num1(n//2)
        num1 = memoize(num1)
        aux = []
        for a in arr:
            aux.append((num1(a), a))
        aux.sort()
        ans = []
        for a in aux:
            ans.append(a[1])
        return ans
