class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        def returnCommon(sta, stb):
            ac = [0]*26
            bc = [0]*26
            for s in sta:
                ac[ord(s)-ord('a')] += 1
            for s in stb:
                bc[ord(s)-ord('a')] += 1
            aux = ''
            for i in range(26):
                aux += chr(ord('a')+i)*min(ac[i], bc[i])
            return aux
        common = returnCommon(A[0], A[0])
        for a in A:
            common = returnCommon(a, common)
        return list(common)
