# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer


def isBadVersion(version):
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not isBadVersion(n):
            return n
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid-1
            else:
                low = mid+1
        while low < n:
            if isBadVersion(low+1):
                break
            low += 1
        return low
