class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        def toBinary(num):
            aux = ''
            while num != 0:
                aux = str(num % 2)+aux
                num = num//2
            return aux
        binary = toBinary(N)
        aux = ''
        for b in binary:
            if b == '1':
                aux += '0'
            else:
                aux += '1'
        ans = 0
        c = 0
        for a in aux[::-1]:
            if a == '1':
                ans += 2**c
            c += 1
        return ans
