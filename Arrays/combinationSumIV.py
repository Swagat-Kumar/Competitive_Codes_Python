class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        def recurr(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            ways = 0
            for z in nums:
                if z <= n:
                    ways += recurr(n-z)
                else:
                    break
            return ways
        recurr = memoize(recurr)
        return recurr(target)
