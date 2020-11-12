class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 2:
            return False
        aux = 1
        n = 2
        while n*n <= num:
            if num % n == 0:
                aux += (n+num//n)
            n += 1
        if aux == num:
            return True
        else:
            return False
