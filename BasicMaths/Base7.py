class Solution:
    def convertToBase7(self, num: int) -> str:
        def convert(n):
            if n == 0:
                return '0'
            aux = ''
            while n != 0:
                aux += str(n % 7)
                n = n//7
            return aux[::-1]
        if num < 0:
            return '-'+convert(-num)
        else:
            return convert(num)
