class Solution:
    def intToRoman(self, num: int) -> str:
        self.aux = ''

        def operate(num, major, minor, maT, miT):
            temp = ''
            temp += (num//major)*maT
            num = num % major
            if num >= minor:
                temp += miT
                num -= minor
            self.aux += temp
            return num
        num = operate(num, 1000, 900, 'M', 'CM')
        num = operate(num, 500, 400, 'D', 'CD')
        num = operate(num, 100, 90, 'C', 'XC')
        num = operate(num, 50, 40, 'L', 'XL')
        num = operate(num, 10, 9, 'X', 'IX')
        num = operate(num, 5, 4, 'V', 'IV')
        self.aux += 'I'*num
        return self.aux
