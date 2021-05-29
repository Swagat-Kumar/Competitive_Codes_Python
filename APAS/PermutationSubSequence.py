class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = 1
        aux = []
        for i in range(1, n):
            factorial *= i
            aux.append(i)
        aux.append(n)
        ans = ""
        k -= 1
        for i in range(n):
            index = k//factorial
            ans += str(aux[index])
            aux.pop(index)
            k = k % factorial
            if i < n-1:
                factorial = factorial//(n-i-1)
        return ans
