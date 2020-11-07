class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def returnBinary(num):
            aux = ''
            while num != 0:
                aux += str(num % 2)
                num = num//2
            return aux
        aux = returnBinary(n)
        for i in range(len(aux)-1):
            if aux[i] == aux[i+1]:
                return False
        return True
