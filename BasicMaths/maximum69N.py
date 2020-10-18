class Solution:
    def maximum69Number(self, num: int) -> int:
        aux = list(str(num))
        for i in range(len(aux)):
            if aux[i] == '6':
                aux[i] = '9'
                return int(''.join(aux))
        return num
