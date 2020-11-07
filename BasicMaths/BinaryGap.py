class Solution:
    def binaryGap(self, n: int) -> int:
        def binary(num):
            aux = ''
            while num != 0:
                aux += str(num % 2)
                num = num//2
            return aux
        aux = binary(n)
        start = 0
        end = 0
        found = False
        ans = 0
        for i in range(len(aux)):
            if aux[i] == '1':
                if not found:
                    start = i
                    found = True
                    continue
                else:
                    if i-start > ans:
                        ans = i-start
                    start = i
        return ans
