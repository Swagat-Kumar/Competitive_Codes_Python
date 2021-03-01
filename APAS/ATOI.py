class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        sign = 1
        i = 0
        st = s.lstrip()
        firstSign = True
        while i < len(st):
            if firstSign and (st[i] == '-' or st[i] == '+'):
                firstSign = False
                if st[i] == '-':
                    sign = -1
            elif st[i].isdigit():
                firstSign = False
                number = number*10+int(st[i])
                if (number > 2**31 and sign == -1):
                    return -2**31
                elif number > 2**31-1 and sign == 1:
                    return 2**31-1
            else:
                break
            i += 1
        return number*sign
