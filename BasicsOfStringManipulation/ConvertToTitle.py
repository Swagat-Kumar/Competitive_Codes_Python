class Solution:
    def convertToTitle(self, n: int) -> str:
        aux = ''
        while n != 0:
            temp = n % 26
            if temp == 0:
                aux = 'Z'+aux
                n = n-26
            else:
                aux = chr(64+temp)+aux
            n = n//26
        return aux
