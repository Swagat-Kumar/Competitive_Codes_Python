class Solution:
    def grayCode(self, n: int):
        ans = [0]
        for i in range(n):
            inc = 1 << i
            for j in range(len(ans)-1, -1, -1):
                ans.append(ans[j]+inc)
        return ans
# My Solution
# class Solution:
#     def grayCode(self, n: int):
#         def toBinary(x):
#             return bin(x)[2:]

#         def toGray(x):
#             aux = x[0]
#             for i in range(len(x)-1):
#                 aux += str(int(x[i]) ^ int(x[i+1]))
#             return aux
#         print(int('0b'+toGray('010'), 2))
#         ans = []
#         for i in range(2**n):
#             ans.append(int('0b'+toGray(toBinary(i)), 2))
#         return ans
