class Solution:
    def restoreIpAddresses(self, s: str):
        ans = []

        def generate(aux, s):
            if len(s) == 0 or len(aux) >= 4:
                if len(aux) == 4 and len(s) == 0:
                    ans.append('.'.join(aux))
                return
            n = int(s[0])
            copy = list(aux)
            copy.append(str(n))
            generate(copy, s[1:])
            if len(s) > 1:
                n = int(s[:2])
                if n > 9:
                    copy = list(aux)
                    copy.append(str(n))
                    generate(copy, s[2:])
            if len(s) > 2:
                n = int(s[:3])
                if n > 99 and n <= 255:
                    copy = list(aux)
                    copy.append(str(n))
                    generate(copy, s[3:])
        generate([], s)
        return ans
