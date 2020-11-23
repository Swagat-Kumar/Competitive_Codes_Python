class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        def canEat(x):
            count = 0
            for p in piles:
                count += p//x
                if p % x > 0:
                    count += 1
                if count > H:
                    return False
            return True
        canEat = memoize(canEat)
        start = 1
        end = max(piles)
        lastFound = max(piles)
        while start <= end:
            mid = (start+end)//2
            if canEat(mid):
                if mid < lastFound:
                    lastFound = mid
                end = mid-1
            else:
                start = mid+1
        return lastFound
