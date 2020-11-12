# SieveofEratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True]*(n)
        p = 2
        while p*p <= n:
            if sieve[p]:
                for j in range(p*p, n, p):
                    sieve[j] = False
            p += 1
        count = 0
        for j in range(2, n):
            if sieve[j]:
                count += 1
        return count
