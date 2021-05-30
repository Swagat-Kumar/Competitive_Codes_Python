class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        if s[0] == 'e' or s[-1] == 'e':
            return False
        if s.count('e') >= 2:
            return False
        if s.count('.') >= 2:
            return False

        num = 0
        for car in s:
            if car.isalpha() and car != 'e':
                return False
            if car.isnumeric():
                num += 1
        if not num:
            return False

        if '.' in s:
            try:
                if not s[s.index('.') + 1].isnumeric() and s[s.index('.') + 1] != 'e':
                    return False
            except IndexError:
                pass

        if 'e' in s:
            e_index: int = s.index('e')
            half1 = s[:e_index]
            half2 = s[e_index+1:]

            if '.' in half2:
                return False
            if not self.isNumber(half1) or not self.isNumber(half2):
                return False

        else:
            if s.count('+') >= 2 or s.count('-') >= 2:
                return False
            if '+' in s or '-' in s:
                if s[0] != '+' and s[0] != '-':
                    return False

        return True
