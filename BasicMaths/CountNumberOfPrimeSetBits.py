class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def check(num):
            aux = bin(num).replace('0b', '')
            count = 0
            for a in aux:
                if a == '1':
                    count += 1
            if count <= 1:
                return False
            for i in range(2, count):
                if count % i == 0:
                    return False
            return True
        ans = 0
        for j in range(L, R+1):
            if check(j):
                ans += 1
        return ans
