class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        k = len(num1)+len(num2)
        ans = [0]*k
        r = 0
        for i in range(len(num2)-1, -1, -1):
            n = int(num2[i])
            for j in range(len(num1)-1, -1, -1):
                p = n*int(num1[j])
                ans[i+j+1] += p
                ans[i+j] += ans[i+j+1]//10
                ans[i+j+1] %= 10
        while len(ans) >= 2 and ans[0] == 0:
            ans.pop(0)
        aux = ''
        for a in ans:
            aux += str(a)
        return aux
