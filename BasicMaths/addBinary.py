class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def toDecimal(st):
            n = 0
            c = 0
            for i in range(len(st)-1, -1, -1):
                n += (2**c)*int(st[i])
                c += 1
            return n

        def toBinary(n):
            if n == 0:
                return '0'
            aux = ''
            while n != 0:
                aux += str(n % 2)
                n = n//2
            return aux[::-1]
        # print(toDecimal(a))
        # print(toDecimal(b))
        sum = toDecimal(a)+toDecimal(b)
        return toBinary(sum)
