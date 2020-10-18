class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            if '0' not in str(i):
                aux = i
                while aux != 0:
                    l = aux % 10
                    if i % l != 0:
                        break
                    aux = aux//10
                if i % l == 0:
                    ans.append(i)
        return ans
