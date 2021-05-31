class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        c = 0
        ans = ''
        while i >= 0 or j >= 0 or c > 0:
            if i >= 0:
                c += int(a[i])
                i -= 1
            if j >= 0:
                c += int(b[j])
                j -= 1
            ans = str(c % 2)+ans
            c = c//2
        return ans


# MyWay
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         def convertToDecimal(a, p=0):
#             if len(a) == 0:
#                 return 0
#             return convertToDecimal(a[:-1], p+1)+int(a[-1])*2**p

#         def convertToBinary(num):
#             if num == 0:
#                 return ''
#             return convertToBinary(num//2)+str(num % 2)
#         ans = convertToDecimal(a)+convertToDecimal(b)
#         if ans == 0:
#             return "0"
#         return convertToBinary(ans)
