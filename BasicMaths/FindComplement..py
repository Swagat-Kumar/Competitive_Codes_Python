class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num).replace('0b', '')
        aux = ''
        for b in binary:
            if b == '1':
                aux += '0'
            else:
                aux += '1'
        return int(aux, 2)
