class Solution:
    def numTrees(self, n: int) -> int:
        def generate(left, right):
            count = 0
            if left >= right:
                return 1
            for i in range(left, right+1):
                count += generate(left, i-1)*generate(i+1, right)
            return count

        def memoize(f):
            memo = {}

            def helper(x, y):
                if str(x)+'|'+str(y) not in memo:
                    memo[str(x)+'|'+str(y)] = f(x, y)
                return memo[str(x)+'|'+str(y)]
            return helper
        generate = memoize(generate)
        return generate(1, n)
