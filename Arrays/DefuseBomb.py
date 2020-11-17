class Solution:
    def decrypt(self, code, k: int):
        ans = list(code)
        if k == 0:
            return [0]*len(code)
        if k < 0:
            for i in range(len(code)):
                summ = 0
                for j in range(-1, k-1, -1):
                    summ += code[i+j]
                ans[i] = summ
        else:
            for i in range(len(code)):
                summ = 0
                for j in range(1, k+1):
                    summ += code[(i+j) % len(code)]
                ans[i] = summ
        return ans
