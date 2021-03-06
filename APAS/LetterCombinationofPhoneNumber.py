class Solution:
    def letterCombinations(self, digits: str):
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        aux = []
        for c in digits:
            if len(aux) == 0:
                for k in dic[c]:
                    aux.append(k)
                continue
            temp = []
            for a in aux:
                for k in dic[c]:
                    temp.append(a+k)
            aux = temp
        return aux
